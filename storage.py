"""
Data Storage & Submission Management
Persists survey responses in SQLite, updates an Excel workbook,
and organizes individual PDF copies.
"""

import os
import json
import sqlite3
import datetime
import zipfile
import io
import pandas as pd
from survey_schema import QUESTIONS, QUESTION_MAP
from pdf_generator import generate_filled_pdf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
PDF_DIR = os.path.join(DATA_DIR, "filled_pdfs")
DB_PATH = os.path.join(DATA_DIR, "survey.db")
CSV_PATH = os.path.join(DATA_DIR, "all_responses.csv")
EXCEL_PATH = os.path.join(DATA_DIR, "all_responses.xlsx")

def init_db():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(PDF_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            submission_id TEXT UNIQUE,
            participant_name TEXT,
            participant_contact TEXT,
            submitted_at TEXT,
            answers_json TEXT,
            pdf_path TEXT
        )
    """)
    conn.commit()
    conn.close()

def _format_answer_readable(qid, val):
    """Converts value(s) into human-readable text."""
    q = QUESTION_MAP.get(qid)
    if not q or not val:
        return ""
    
    val_to_text = {opt["value"]: f"{opt['text_en']} / {opt['text_hi']}" for opt in q["options"]}
    
    if isinstance(val, list):
        return "; ".join([val_to_text.get(v, v) for v in val])
    return val_to_text.get(val, val)

def save_submission(participant_name, participant_contact, answers):
    """
    Saves a new submission, generates its official filled PDF,
    and updates the database and Excel file.
    """
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM submissions")
    count = cur.fetchone()[0] + 1
    
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M")
    date_code = now.strftime("%Y%m%d")
    sub_id = f"RESP-{date_code}-{count:03d}"
    
    clean_name = (participant_name or "Anonymous").strip()
    safe_name = "".join([c for c in clean_name if c.isalnum() or c in " _-"]).strip() or "Participant"
    pdf_filename = f"{sub_id}_{safe_name}.pdf"
    pdf_full_path = os.path.join(PDF_DIR, pdf_filename)

    submission_dict = {
        "submission_id": sub_id,
        "participant_name": clean_name,
        "participant_contact": (participant_contact or "").strip(),
        "submitted_at": date_str,
        "answers": answers
    }

    # Generate and save filled PDF
    generate_filled_pdf(submission_dict, output_path=pdf_full_path)

    # Optional: Send automatic email with attached PDF (if SMTP configured)
    try:
        from email_notifier import send_submission_email
        send_submission_email(submission_dict, pdf_full_path)
    except Exception as e:
        print("Email notify skipped/error:", e)

    # Insert into SQLite
    cur.execute("""
        INSERT INTO submissions (submission_id, participant_name, participant_contact, submitted_at, answers_json, pdf_path)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        sub_id,
        clean_name,
        participant_contact,
        date_str,
        json.dumps(answers, ensure_ascii=False),
        pdf_full_path
    ))
    conn.commit()
    conn.close()

    # Rebuild Excel summary
    update_excel_export()

    return {
        "submission_id": sub_id,
        "participant_name": clean_name,
        "pdf_filename": pdf_filename,
        "pdf_path": pdf_full_path,
        "submitted_at": date_str
    }

def get_submission(submission_id):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM submissions WHERE submission_id = ?", (submission_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        d = dict(row)
        d["answers"] = json.loads(d["answers_json"])
        return d
    return None

def get_all_submissions():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM submissions ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    results = []
    for r in rows:
        d = dict(r)
        d["answers"] = json.loads(d["answers_json"])
        results.append(d)
    return results

def update_excel_export():
    """Generates an up-to-date Excel and CSV sheet with all answers in neat columns."""
    subs = get_all_submissions()
    if not subs:
        return
    
    rows = []
    for s in reversed(subs): # chronological
        row = {
            "Submission ID": s["submission_id"],
            "Submitted At": s["submitted_at"],
            "Participant Name": s["participant_name"],
            "Contact Info": s["participant_contact"]
        }
        ans = s["answers"]
        for q in QUESTIONS:
            col_name = f"Q{q['number']}: {q['text_en']}"
            val = ans.get(q["id"])
            row[col_name] = _format_answer_readable(q["id"], val)
        rows.append(row)

    df = pd.DataFrame(rows)
    df.to_csv(CSV_PATH, index=False, encoding="utf-8-sig")
    try:
        df.to_excel(EXCEL_PATH, index=False)
    except Exception as e:
        print("Excel write exception (CSV saved):", e)

def create_zip_of_all_pdfs():
    """Zips all generated PDFs and returns memory bytes."""
    mem_zip = io.BytesIO()
    with zipfile.ZipFile(mem_zip, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        if os.path.exists(PDF_DIR):
            for fname in os.listdir(PDF_DIR):
                if fname.endswith(".pdf"):
                    fpath = os.path.join(PDF_DIR, fname)
                    zf.write(fpath, arcname=fname)
    mem_zip.seek(0)
    return mem_zip.getvalue()

"""
Data Storage & Submission Management
Supports both SQLite (local default) and PostgreSQL (for persistent cloud storage on Render).
Includes on-the-fly PDF generation and database diagnostics.
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
EXCEL_PATH = os.path.join(DATA_DIR, "all_responses.xlsx")
CSV_PATH = os.path.join(DATA_DIR, "all_responses.csv")

def get_raw_database_url():
    url = os.environ.get("DATABASE_URL", "").strip().strip("'").strip('"')
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)
    return url

def is_postgres():
    return bool(get_raw_database_url())

def get_db_status():
    """Returns database type and connection health for admin dashboard."""
    raw_url = get_raw_database_url()
    if not raw_url:
        return {
            "type": "SQLite (Temporary Storage)",
            "is_permanent": False,
            "message": "Temporary storage. Connect DATABASE_URL in Render to make permanent."
        }
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1")
        conn.close()
        return {
            "type": "PostgreSQL (Permanent Cloud Storage)",
            "is_permanent": True,
            "message": "Connected successfully! All survey responses are permanently preserved."
        }
    except Exception as e:
        return {
            "type": "PostgreSQL Connection Error",
            "is_permanent": False,
            "message": f"Connection failed: {str(e)}"
        }

def get_connection():
    raw_url = get_raw_database_url()
    if raw_url:
        import psycopg2
        import psycopg2.extras
        # Try normal connect, or with sslmode=require if needed
        try:
            conn = psycopg2.connect(raw_url)
            return conn
        except Exception as e:
            if "sslmode" not in raw_url.lower():
                delim = "&" if "?" in raw_url else "?"
                return psycopg2.connect(raw_url + delim + "sslmode=require")
            raise e
    else:
        os.makedirs(DATA_DIR, exist_ok=True)
        os.makedirs(PDF_DIR, exist_ok=True)
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

def init_db():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(PDF_DIR, exist_ok=True)
    try:
        conn = get_connection()
        cur = conn.cursor()
        if is_postgres():
            cur.execute("""
                CREATE TABLE IF NOT EXISTS submissions (
                    id SERIAL PRIMARY KEY,
                    submission_id TEXT UNIQUE,
                    participant_name TEXT,
                    participant_contact TEXT,
                    submitted_at TEXT,
                    answers_json TEXT,
                    pdf_path TEXT
                )
            """)
        else:
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
    except Exception as e:
        print("Database initialization error:", e)

def _format_answer_readable(qid, val):
    q = QUESTION_MAP.get(qid)
    if not q or not val:
        return ""
    val_to_text = {opt["value"]: f"{opt['text_en']} / {opt['text_hi']}" for opt in q["options"]}
    if isinstance(val, list):
        return "; ".join([val_to_text.get(v, v) for v in val])
    return val_to_text.get(val, val)

def save_submission(participant_name, participant_contact, answers):
    init_db()
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM submissions")
    row = cur.fetchone()
    count = (row[0] if isinstance(row, tuple) else row["COUNT(*)"] if "COUNT(*)" in row else row[0]) + 1

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
    try:
        generate_filled_pdf(submission_dict, output_path=pdf_full_path)
    except Exception as e:
        print("PDF generation error:", e)

    # Optional: Send automatic email with attached PDF (if SMTP configured)
    try:
        from email_notifier import send_submission_email
        send_submission_email(submission_dict, pdf_full_path)
    except Exception as e:
        print("Email notify skipped/error:", e)

    # Insert into Database
    placeholder = "%s" if is_postgres() else "?"
    query = f"""
        INSERT INTO submissions (submission_id, participant_name, participant_contact, submitted_at, answers_json, pdf_path)
        VALUES ({placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder})
    """
    cur.execute(query, (
        sub_id,
        clean_name,
        participant_contact,
        date_str,
        json.dumps(answers, ensure_ascii=False),
        pdf_full_path
    ))
    conn.commit()
    conn.close()

    # Rebuild Excel & CSV
    try:
        update_excel_export()
    except Exception as e:
        print("Excel update error:", e)

    return {
        "submission_id": sub_id,
        "participant_name": clean_name,
        "pdf_filename": pdf_filename,
        "pdf_path": pdf_full_path,
        "submitted_at": date_str
    }

def get_submission(submission_id):
    init_db()
    conn = get_connection()
    if is_postgres():
        import psycopg2.extras
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM submissions WHERE submission_id = %s", (submission_id,))
    else:
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
    conn = get_connection()
    if is_postgres():
        import psycopg2.extras
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM submissions ORDER BY id DESC")
    else:
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

def ensure_pdf_exists(sub):
    """
    Ensures that the filled PDF for a submission exists on disk.
    If missing (e.g. after container restart), regenerates it dynamically!
    """
    os.makedirs(PDF_DIR, exist_ok=True)
    safe_name = "".join([c for c in sub["participant_name"] if c.isalnum() or c in " _-"]).strip() or "Participant"
    pdf_filename = f"{sub['submission_id']}_{safe_name}.pdf"
    pdf_path = os.path.join(PDF_DIR, pdf_filename)
    
    if not os.path.exists(pdf_path):
        submission_dict = {
            "submission_id": sub["submission_id"],
            "participant_name": sub["participant_name"],
            "participant_contact": sub.get("participant_contact", ""),
            "submitted_at": sub.get("submitted_at", ""),
            "answers": sub.get("answers", {})
        }
        generate_filled_pdf(submission_dict, output_path=pdf_path)
    return pdf_path

def update_excel_export():
    subs = get_all_submissions()
    if not subs:
        return
    rows = []
    for s in reversed(subs):
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
    os.makedirs(DATA_DIR, exist_ok=True)
    df.to_csv(CSV_PATH, index=False, encoding="utf-8-sig")
    try:
        df.to_excel(EXCEL_PATH, index=False)
    except Exception as e:
        print("Excel write exception (CSV saved):", e)

def create_zip_of_all_pdfs():
    subs = get_all_submissions()
    mem_zip = io.BytesIO()
    with zipfile.ZipFile(mem_zip, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        for s in subs:
            pdf_path = ensure_pdf_exists(s)
            if os.path.exists(pdf_path):
                zf.write(pdf_path, arcname=os.path.basename(pdf_path))
    mem_zip.seek(0)
    return mem_zip.getvalue()

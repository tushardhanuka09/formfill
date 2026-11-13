"""
Flask Application for AcSIR Societal Program Survey
Provides:
  - Online Public Survey Form (mobile-optimized, bilingual)
  - Automatic PDF Generator (marks original PDF checkboxes)
  - Individual PDF Download for participant and organizer ("Form by Form")
  - Organizer Dashboard with Excel and All-PDFs ZIP export
"""

import os
from flask import (
    Flask, render_template, request, redirect, url_for,
    send_file, session, flash, Response
)
from survey_schema import SURVEY_METADATA, SECTIONS, QUESTIONS, QUESTION_MAP
import storage

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "acsir-screen-habit-survey-secret-2026")

ADMIN_PIN = os.environ.get("ADMIN_PIN", "admin123")

@app.route("/")
def survey_form():
    """Renders the official online survey."""
    return render_template(
        "survey.html",
        metadata=SURVEY_METADATA,
        sections=SECTIONS,
        questions=QUESTIONS
    )

@app.route("/submit", methods=["POST"])
def submit_survey():
    """Processes survey submission and generates the stamped PDF."""
    participant_name = request.form.get("participant_name", "").strip() or "Anonymous"
    participant_contact = request.form.get("participant_contact", "").strip()

    answers = {}
    for q in QUESTIONS:
        qid = q["id"]
        if q["type"] == "checkbox":
            # list of values
            answers[qid] = request.form.getlist(f"{qid}[]")
        else:
            answers[qid] = request.form.get(qid, "")

    # Save to storage (DB, Excel, and filled PDF generation)
    record = storage.save_submission(participant_name, participant_contact, answers)
    return redirect(url_for("thank_you", submission_id=record["submission_id"]))

@app.route("/thank-you/<submission_id>")
def thank_you(submission_id):
    """Post-submission confirmation page with instant PDF download."""
    sub = storage.get_submission(submission_id)
    if not sub:
        return redirect(url_for("survey_form"))
    return render_template("success.html", submission=sub)

@app.route("/download/<submission_id>")
def download_pdf(submission_id):
    """Downloads an individual respondent's filled PDF form."""
    sub = storage.get_submission(submission_id)
    if not sub:
        return "Submission not found", 404
    
    # Automatically regenerates the PDF on the fly if container restarted!
    pdf_path = storage.ensure_pdf_exists(sub)
    if not os.path.exists(pdf_path):
        return "PDF not found for this response", 404
    
    clean_name = "".join([c for c in sub["participant_name"] if c.isalnum() or c in " _-"]).strip()
    download_name = f"AcSIR_Survey_{sub['submission_id']}_{clean_name}.pdf"
    return send_file(
        pdf_path,
        as_attachment=True,
        download_name=download_name,
        mimetype="application/pdf"
    )

# --- Admin Routes ---

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        pin = request.form.get("password", "")
        if pin == ADMIN_PIN:
            session["is_admin"] = True
            return redirect(url_for("admin_dashboard"))
        return render_template("login.html", error="Invalid PIN. Default PIN is 'admin123'")
    return render_template("login.html")

@app.route("/admin/logout")
def admin_logout():
    session.pop("is_admin", None)
    return redirect(url_for("admin_login"))

@app.route("/admin")
def admin_dashboard():
    if not session.get("is_admin"):
        return redirect(url_for("admin_login"))
    submissions = storage.get_all_submissions()
    return render_template("admin.html", submissions=submissions)

@app.route("/admin/export/excel")
def admin_export_excel():
    if not session.get("is_admin"):
        return redirect(url_for("admin_login"))
    storage.update_excel_export()
    if not os.path.exists(storage.EXCEL_PATH):
        return "No submissions available to export yet", 404
    return send_file(
        storage.EXCEL_PATH,
        as_attachment=True,
        download_name="AcSIR_All_Survey_Responses.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

@app.route("/admin/export/zip")
def admin_download_all_zip():
    if not session.get("is_admin"):
        return redirect(url_for("admin_login"))
    zip_bytes = storage.create_zip_of_all_pdfs()
    return Response(
        zip_bytes,
        mimetype="application/zip",
        headers={"Content-Disposition": "attachment;filename=All_Completed_Survey_PDFs.zip"}
    )

if __name__ == "__main__":
    storage.init_db()
    port = int(os.environ.get("PORT", 5000))
    print(f"Server starting on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)


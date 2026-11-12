# AcSIR Survey Web Application & Individual PDF Generator
### Societal Program: Problem Understanding and Analysis (AcSIR-04-SP)
**Screen Use Behaviour, Digital Habits and Visual Well-being**  
*(स्क्रीन उपयोग व्यवहार, डिजिटल आदतें और दृश्य कल्याण)*

---

## 🌟 What This System Does

1. **Circulate Online**: A clean, mobile-responsive online survey that anyone can fill on their phone or laptop.
2. **Exact PDF Output**: Stretches over all 9 pages of `last final print.pdf` with **real vector checkmarks (`✔`)** placed inside the exact physical boxes.
3. **Form by Form Individual Downloads**:
   - **For Respondents**: An instant "Download Filled PDF" button right after submission.
   - **For Organizers**: An Admin Portal where you can download each participant's filled PDF individually (`RESP-001.pdf`, `RESP-002.pdf`, etc.), download **All PDFs as a ZIP**, and download the **Master Excel Sheet (`.xlsx`)**.
4. **Google Forms Backup**: Includes `create_google_form.js` to create the exact 23-question form in your Google Drive with 1 click.
5. **Interactive Fillable PDF**: Includes `fillable_survey.pdf` with clickable checkboxes for offline PDF filling.

---

## 🚀 Quick Start (Run Locally on Windows)

Simply **double-click** the file:
```
run_survey_app.bat
```
This starts the local web server and opens:
- **Public Survey Link**: `http://localhost:5000/`
- **Organizer Admin Portal**: `http://localhost:5000/admin` *(Default PIN: `admin123`)*

---

## 🌐 How to Host Online for Free (Share on WhatsApp)

To share a public link with anyone on the internet, deploy it for **100% free** in 3 minutes on **Render.com**:

1. Create a free account at [Render.com](https://render.com/).
2. Push or upload this folder to GitHub (or use Render's direct Web Service).
3. Choose **"New +" -> "Web Service"**.
4. Set:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app` (or `python app.py`)
5. Render gives you a free public link like `https://acsir-screen-survey.onrender.com` that you can send to anyone!

*(Alternative free hosts: PythonAnywhere.com, Streamlit Cloud, Railway, or Hugging Face Spaces).*

---

## 📁 Project File Structure

- `last final print.pdf`: The master 9-page research survey document.
- `app.py`: Flask web application routes & views.
- `pdf_generator.py`: Precision coordinate PDF stamper using PyMuPDF.
- `storage.py`: SQLite database, Excel exporter, and ZIP packager.
- `survey_schema.py`: Complete bilingual question definitions and coordinate mappings.
- `fillable_survey.pdf`: Interactive digital PDF with clickable checkboxes.
- `create_google_form.js`: 1-click Google Apps Script to auto-generate the Google Form.
- `run_survey_app.bat`: Windows 1-click launcher.
- `data/`: Stores submitted responses, Excel spreadsheets, and generated filled PDFs.


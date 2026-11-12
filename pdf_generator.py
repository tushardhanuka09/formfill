"""
PDF Stamping and Generation Module
Overlays responses onto the original 'last final print.pdf' template.
"""

import os
import pymupdf
from survey_schema import QUESTIONS

TEMPLATE_PDF = os.path.join(os.path.dirname(__file__), "last final print.pdf")

def _get_page_box_rects(doc):
    """
    Returns a dictionary mapping page_num (2-9) to a list of sorted Rects of '☐'.
    """
    box_rects = {}
    for pno in range(1, len(doc)):
        page = doc[pno]
        box_words = [w for w in page.get_text("words") if w[4] == "☐"]
        box_words.sort(key=lambda w: (round(w[1], -1), w[0]))
        box_rects[pno + 1] = [pymupdf.Rect(w[0], w[1], w[2], w[3]) for w in box_words]
    return box_rects

def _draw_checkmark(page, rect, color=(0.0, 0.32, 0.75)):
    """
    Draws a sharp, professional checkmark vector inside the checkbox rect.
    """
    w = rect.width
    h = rect.height
    cx = (rect.x0 + rect.x1) / 2
    cy = (rect.y0 + rect.y1) / 2

    p1 = pymupdf.Point(rect.x0 + w * 0.20, cy)
    p2 = pymupdf.Point(rect.x0 + w * 0.44, rect.y1 - h * 0.18)
    p3 = pymupdf.Point(rect.x1 - w * 0.12, rect.y0 + h * 0.16)

    shape = page.new_shape()
    shape.draw_line(p1, p2)
    shape.draw_line(p2, p3)
    shape.finish(color=color, width=1.75, stroke_opacity=1.0)
    shape.commit()

def generate_filled_pdf(submission_data, output_path=None):
    """
    Generates a completed PDF for a given submission.
    """
    if not os.path.exists(TEMPLATE_PDF):
        raise FileNotFoundError(f"Template PDF not found: {TEMPLATE_PDF}")

    doc = pymupdf.open(TEMPLATE_PDF)
    box_rects_by_page = _get_page_box_rects(doc)

    # 1. Stamp Header / Participant info on Page 2 (index 1) right above the blue divider line
    p_name = submission_data.get("participant_name") or "Anonymous Participant"
    p_id = submission_data.get("submission_id", "RESP-001")
    p_date = submission_data.get("submitted_at", "")
    p_contact = submission_data.get("participant_contact", "")

    page2 = doc[1]
    
    meta_parts = [f"ID: {p_id}", f"Participant: {p_name}"]
    if p_contact:
        meta_parts.append(f"Contact: {p_contact}")
    if p_date:
        meta_parts.append(f"Date: {p_date}")
    meta_line = "   |   ".join(meta_parts)
    
    font_size = 8.5
    text_width = pymupdf.get_text_length(meta_line, fontname="helv", fontsize=font_size)
    start_x = max(40.0, (page2.rect.width - text_width) / 2.0)
    
    # Stamp cleanly centered at y=153
    page2.insert_text(
        pymupdf.Point(start_x, 153),
        meta_line,
        fontsize=font_size,
        fontname="helv",
        color=(0.10, 0.25, 0.55)
    )

    # 2. Iterate through submitted answers and stamp checkmarks
    answers = submission_data.get("answers", {})

    for q in QUESTIONS:
        qid = q["id"]
        val = answers.get(qid)
        if not val:
            continue

        selected_values = val if isinstance(val, list) else [val]

        for opt in q["options"]:
            if opt["value"] in selected_values:
                page_num = opt["page"]
                box_idx = opt["box_idx"]
                
                target_page = doc[page_num - 1]
                boxes_on_page = box_rects_by_page.get(page_num, [])
                
                if 0 <= box_idx < len(boxes_on_page):
                    rect = boxes_on_page[box_idx]
                    _draw_checkmark(target_page, rect)

    if output_path:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        doc.save(output_path)
        doc.close()
        return output_path
    else:
        pdf_bytes = doc.tobytes()
        doc.close()
        return pdf_bytes

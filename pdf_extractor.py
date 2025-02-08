# pdf_extractor.py - Extract PDF Data
import fitz

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    return "\n".join([page.get_text() for page in doc])


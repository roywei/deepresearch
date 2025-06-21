import io
from typing import List
from PyPDF2 import PdfReader


def read_pdf_text(path: str) -> str:
    """Extract text from a PDF file."""
    reader = PdfReader(path)
    text = []
    for page in reader.pages:
        text.append(page.extract_text())
    return "\n".join(text)

"""Extract text from PDFs."""

import fitz
import os
from pathlib import Path
from src.aws_utils import download_from_s3
import logging

logger = logging.getLogger(__name__)


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a PDF file.

    Args:
        pdf_path: Path to PDF file

    Returns:
        Extracted text
    """
    pdf_path = Path(pdf_path)
    # Optional: Download from S3 if configured
    if os.getenv("AWS_S3_BUCKET") and os.getenv("AWS_S3_KEY"):
        download_from_s3(
            bucket=os.getenv("AWS_S3_BUCKET"),
            key=os.getenv("AWS_S3_KEY"),
            local_path=pdf_path,
        )
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text() for page in doc])
        logger.info(f"Extracted text from {pdf_path}")
        return text
    except Exception as e:
        logger.error(f"PDF extraction failed: {e}")
        raise

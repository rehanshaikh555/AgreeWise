from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

APP_NAME = "AgreeWise"
APP_TAGLINE = "Understand before you agree."

SUPPORTED_TEXT_TYPES = {
    "text/plain": ".txt",
}

SUPPORTED_DOCUMENT_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt",
    ".jpg",
    ".jpeg",
    ".png",
}

MAX_TEXT_LENGTH = 1_000_000

OCR_AVAILABLE = False

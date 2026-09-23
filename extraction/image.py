import shutil
from pathlib import Path

from PIL import Image
import pytesseract


def is_ocr_available() -> bool:
    return shutil.which("tesseract") is not None


def extract_image(source: str | Path | bytes) -> str:
    if not is_ocr_available():
        raise RuntimeError(
            "OCR is unavailable because the Tesseract executable "
            "is not installed or cannot be found."
        )

    if isinstance(source, bytes):
        import io
        image = Image.open(io.BytesIO(source))
    else:
        image = Image.open(source)

    return pytesseract.image_to_string(image).strip()

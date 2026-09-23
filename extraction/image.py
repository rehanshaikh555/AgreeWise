import io
import os
import shutil
from pathlib import Path

from PIL import Image
import pytesseract


DEFAULT_TESSERACT_PATH = (
    Path.home()
    / ".local"
    / "opt"
    / "tesseract-native"
    / "bin"
    / "tesseract"
)

DEFAULT_TESSDATA_PATH = (
    Path.home()
    / ".local"
    / "opt"
    / "tesseract-native"
    / "share"
    / "tessdata"
)

DEFAULT_TESSERACT_LIB_PATH = (
    Path.home()
    / ".local"
    / "opt"
    / "tesseract-native"
    / "lib"
)

DEFAULT_LEPTONICA_LIB_PATH = (
    Path.home()
    / ".local"
    / "opt"
    / "leptonica"
    / "lib"
)


def _find_tesseract() -> str | None:
    """Find the Tesseract executable used by AgreeWise."""

    configured = os.environ.get("TESSERACT_CMD")
    if configured and Path(configured).is_file():
        return configured

    system_tesseract = shutil.which("tesseract")
    if system_tesseract:
        return system_tesseract

    if DEFAULT_TESSERACT_PATH.is_file():
        return str(DEFAULT_TESSERACT_PATH)

    return None


def _configure_tesseract() -> str:
    """Configure pytesseract for the local AgreeWise OCR installation."""

    tesseract_cmd = _find_tesseract()

    if not tesseract_cmd:
        raise RuntimeError(
            "OCR is unavailable because the Tesseract executable "
            "could not be found."
        )

    tessdata_path = os.environ.get(
        "TESSDATA_PREFIX",
        str(DEFAULT_TESSDATA_PATH),
    )

    if not Path(tessdata_path).is_dir():
        raise RuntimeError(
            "OCR is unavailable because the Tesseract language-data "
            f"directory was not found: {tessdata_path}"
        )

    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    os.environ["TESSDATA_PREFIX"] = tessdata_path

    library_paths = [
        str(DEFAULT_TESSERACT_LIB_PATH),
        str(DEFAULT_LEPTONICA_LIB_PATH),
    ]

    existing_ld_path = os.environ.get("LD_LIBRARY_PATH", "")
    combined_paths = library_paths + (
        [existing_ld_path] if existing_ld_path else []
    )

    os.environ["LD_LIBRARY_PATH"] = ":".join(combined_paths)

    return tesseract_cmd


def is_ocr_available() -> bool:
    """Return True when Tesseract and its language data are available."""

    try:
        _configure_tesseract()
        return True
    except RuntimeError:
        return False


def get_available_languages() -> list[str]:
    """Return languages currently available to Tesseract."""

    _configure_tesseract()

    try:
        output = pytesseract.get_languages(config="")
    except pytesseract.TesseractError as exc:
        raise RuntimeError(
            f"Unable to read installed OCR languages: {exc}"
        ) from exc

    return sorted(output)


def extract_image(
    source: str | Path | bytes,
    language: str = "auto",
) -> str:
    """Extract text from an image using Tesseract OCR."""

    _configure_tesseract()

    available_languages = get_available_languages()

    if language == "auto":
        preferred_languages = ["eng", "hin", "mar"]
        requested_languages = [
            item
            for item in preferred_languages
            if item in available_languages
        ]

        if not requested_languages:
            raise RuntimeError(
                "OCR is unavailable because no supported OCR "
                "language model is installed."
            )

        language = "+".join(requested_languages)
    else:
        requested_languages = [
        item.strip()
        for item in language.split("+")
        if item.strip()
    ]

    missing_languages = [
        item
        for item in requested_languages
        if item not in available_languages
    ]

    if missing_languages:
        raise ValueError(
            "Requested OCR language(s) are not installed: "
            + ", ".join(missing_languages)
        )

    if isinstance(source, bytes):
        image = Image.open(io.BytesIO(source))
    else:
        image = Image.open(source)

    image = image.convert("RGB")

    try:
        text = pytesseract.image_to_string(
            image,
            lang=language,
            config="--psm 6",
        )
    except pytesseract.TesseractError as exc:
        raise RuntimeError(
            f"OCR processing failed: {exc}"
        ) from exc

    return text.strip()

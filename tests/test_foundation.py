from config.settings import (
    APP_NAME,
    APP_TAGLINE,
    SUPPORTED_DOCUMENT_EXTENSIONS,
)


def test_app_identity():
    assert APP_NAME == "AgreeWise"
    assert APP_TAGLINE == "Understand before you agree."


def test_supported_documents():
    assert ".pdf" in SUPPORTED_DOCUMENT_EXTENSIONS
    assert ".docx" in SUPPORTED_DOCUMENT_EXTENSIONS
    assert ".txt" in SUPPORTED_DOCUMENT_EXTENSIONS
    assert ".jpg" in SUPPORTED_DOCUMENT_EXTENSIONS
    assert ".png" in SUPPORTED_DOCUMENT_EXTENSIONS

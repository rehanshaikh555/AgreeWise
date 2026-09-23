from pathlib import Path

import pymupdf


def extract_pdf(source: str | Path | bytes) -> str:
    if isinstance(source, bytes):
        document = pymupdf.open(
            stream=source,
            filetype="pdf",
        )
    else:
        document = pymupdf.open(str(source))

    try:
        pages = []

        for page in document:
            text = page.get_text("text")

            if text:
                pages.append(text)

        return "\n\n".join(pages).strip()

    finally:
        document.close()

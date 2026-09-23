from pathlib import Path

from extraction.docx import extract_docx
from extraction.image import extract_image
from extraction.pdf import extract_pdf
from extraction.txt import extract_txt


SUPPORTED_EXTENSIONS = {'.txt', '.pdf', '.docx', '.jpg', '.jpeg', '.png'}


def extract_text_from_file(source, filename=None):
    if filename:
        extension = Path(filename).suffix.lower()
    elif isinstance(source, (str, Path)):
        extension = Path(source).suffix.lower()
    else:
        raise ValueError('filename is required when source is provided as bytes.')

    if extension == '.txt':
        return extract_txt(source)
    if extension == '.pdf':
        return extract_pdf(source)
    if extension == '.docx':
        return extract_docx(source)
    if extension in {'.jpg', '.jpeg', '.png'}:
        return extract_image(source)

    raise ValueError(f'Unsupported document type: {extension or "unknown"}')


def normalize_text(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    text = text.replace(chr(13) + chr(10), chr(10))
    text = text.replace(chr(13), chr(10))

    lines = []

    for line in text.split(chr(10)):
        cleaned = ' '.join(line.split())
        if cleaned:
            lines.append(cleaned)

    return chr(10).join(lines).strip()


def extract_and_normalize(source, filename=None):
    if isinstance(source, str) and filename and (chr(10) in source or chr(13) in source):
        text = source
    else:
        text = extract_text_from_file(source, filename)

    return normalize_text(text)

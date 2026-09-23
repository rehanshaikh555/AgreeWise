import re


def analyze_metadata(text: str) -> dict:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    stripped = text.strip()

    words = re.findall(r"\b[\w'-]+\b", stripped, flags=re.UNICODE)

    sentences = [
        s.strip()
        for s in re.split(r"(?<=[.!?।])\s+", stripped)
        if s.strip()
    ]

    paragraphs = [
        p.strip()
        for p in re.split(r"\n\s*\n", stripped)
        if p.strip()
    ]

    return {
        "character_count": len(stripped),
        "word_count": len(words),
        "sentence_count": len(sentences),
        "paragraph_count": len(paragraphs),
        "is_empty": not bool(stripped),
    }

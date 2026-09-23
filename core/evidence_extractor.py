import re


def split_sentences(text: str) -> list[str]:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentences = []

    for block in re.split(r"\n\s*\n|\n", text.strip()):
        block = block.strip()

        if not block:
            continue

        parts = re.split(r"(?<=[.!?।])\s+", block)

        for sentence in parts:
            sentence = sentence.strip()

            if sentence:
                sentences.append(sentence)

    return sentences


def extract_evidence(
    text: str,
    matches: list[str],
    primary_phrases: list[str] | None = None,
) -> list[dict]:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not isinstance(matches, list):
        raise TypeError("matches must be a list")

    if primary_phrases is not None and not isinstance(primary_phrases, list):
        raise TypeError("primary_phrases must be a list or None")

    sentences = split_sentences(text)
    evidence = []

    for sentence in sentences:
        lowered_sentence = sentence.lower()

        matched_keywords = [
            keyword
            for keyword in matches
            if keyword.lower() in lowered_sentence
        ]

        if not matched_keywords:
            continue

        if primary_phrases:
            matched_primary = [
                phrase
                for phrase in primary_phrases
                if phrase.lower() in lowered_sentence
            ]

            if not matched_primary:
                continue
        else:
            matched_primary = []

        evidence.append(
            {
                "sentence": sentence,
                "matches": matched_keywords,
                "primary_matches": matched_primary,
            }
        )

    return evidence

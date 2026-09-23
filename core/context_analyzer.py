import re


NEGATION_PATTERNS = [
    r"\bdo not\b",
    r"\bdoes not\b",
    r"\bdid not\b",
    r"\bnever\b",
    r"\bnot\b",
    r"\bno\b",
    r"\bwithout\b",
]

CONDITIONAL_PATTERNS = [
    r"\bmay\b",
    r"\bmight\b",
    r"\bcould\b",
    r"\bwhere permitted\b",
    r"\bif you\b",
    r"\bwith your consent\b",
    r"\bsubject to\b",
]


def _find_indicators(sentence: str, patterns: list[str]) -> list[str]:
    lowered = sentence.lower()

    indicators = []

    for pattern in patterns:
        if re.search(pattern, lowered):
            match = re.search(pattern, lowered)
            if match:
                indicators.append(match.group(0))

    return indicators


def analyze_context(sentence: str) -> dict:
    if not isinstance(sentence, str):
        raise TypeError("sentence must be a string")

    cleaned = " ".join(sentence.split())

    if not cleaned:
        return {
            "context": "unknown",
            "label": "Unknown",
            "indicators": [],
        }

    negation_matches = _find_indicators(
        cleaned,
        NEGATION_PATTERNS,
    )

    conditional_matches = _find_indicators(
        cleaned,
        CONDITIONAL_PATTERNS,
    )

    if negation_matches:
        return {
            "context": "negative",
            "label": "Explicitly not stated",
            "indicators": negation_matches,
        }

    if conditional_matches:
        return {
            "context": "conditional",
            "label": "Conditional",
            "indicators": conditional_matches,
        }

    return {
        "context": "stated",
        "label": "Stated practice",
        "indicators": [],
    }

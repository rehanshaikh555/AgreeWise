import re


DOCUMENT_TYPES = {
    "privacy_policy": "Privacy Policy",
    "terms": "Terms & Conditions",
    "cookie_policy": "Cookie Policy",
    "user_agreement": "User Agreement",
    "unknown": "Unknown",
}


EXACT_HEADINGS = {
    "privacy_policy": [
        "privacy policy",
        "privacy notice",
        "data privacy policy",
    ],
    "terms": [
        "terms and conditions",
        "terms of service",
        "terms of use",
    ],
    "cookie_policy": [
        "cookie policy",
        "cookies policy",
    ],
    "user_agreement": [
        "user agreement",
        "end user agreement",
        "subscriber agreement",
    ],
}


KEYWORDS = {
    "privacy_policy": [
        "personal data",
        "personal information",
        "data we collect",
        "information we collect",
        "how we use your information",
        "data protection",
    ],
    "terms": [
        "use of the service",
        "agreement between you",
        "acceptable use",
    ],
    "cookie_policy": [
        "cookies",
        "web beacons",
        "tracking technologies",
        "similar technologies",
    ],
    "user_agreement": [
        "user terms",
        "license agreement",
    ],
}


def detect_document_type(text: str) -> dict:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned = re.sub(r"\s+", " ", text.lower()).strip()

    if not cleaned:
        return {
            "type": "unknown",
            "name": DOCUMENT_TYPES["unknown"],
            "confidence": 0.0,
            "matches": [],
        }

    # Explicit document titles/headings get priority.
    for document_type, headings in EXACT_HEADINGS.items():
        for heading in headings:
            if re.search(
                rf"(^|\s){re.escape(heading)}(\s|$|[:\-])",
                cleaned,
            ):
                return {
                    "type": document_type,
                    "name": DOCUMENT_TYPES[document_type],
                    "confidence": 1.0,
                    "matches": [heading],
                }

    scores = {}

    for document_type, keywords in KEYWORDS.items():
        matches = [
            keyword
            for keyword in keywords
            if keyword in cleaned
        ]
        scores[document_type] = matches

    ranked = sorted(
        scores.items(),
        key=lambda item: len(item[1]),
        reverse=True,
    )

    best_type, best_matches = ranked[0]

    if not best_matches:
        return {
            "type": "unknown",
            "name": DOCUMENT_TYPES["unknown"],
            "confidence": 0.0,
            "matches": [],
        }

    confidence = min(
        0.95,
        0.35 + (len(best_matches) * 0.15),
    )

    return {
        "type": best_type,
        "name": DOCUMENT_TYPES[best_type],
        "confidence": round(confidence, 2),
        "matches": best_matches,
    }

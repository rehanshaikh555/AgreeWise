import re


CLAUSE_CATEGORIES = {
    "personal_data": {
        "name": "Personal Data",
        "keywords": [
            "personal data",
            "personal information",
            "name",
            "email address",
            "phone number",
            "contact information",
            "date of birth",
            "identity",
        ],
    },
    "location": {
        "name": "Location",
        "keywords": [
            "location data",
            "location information",
            "your location",
            "gps",
            "geolocation",
            "precise location",
            "approximate location",
        ],
    },
    "tracking": {
        "name": "Cookies & Tracking",
        "keywords": [
            "cookies",
            "cookie",
            "tracking technologies",
            "web beacons",
            "pixels",
            "tracking",
        ],
    },
    "third_party_sharing": {
        "name": "Third-party Sharing",
        "keywords": [
            "third parties",
            "third-party",
            "service providers",
            "business partners",
            "share your information",
            "disclose your information",
            "vendors",
        ],
    },
    "retention": {
        "name": "Data Retention",
        "keywords": [
            "retain your data",
            "retain your information",
            "retain your personal information",
            "data retention",
            "retention period",
            "how long we keep",
            "store your information",
            "stored for as long",
            "stored for",
            "keep your information",
            "keep your data",
            "for as long as necessary",
        ],
    },
    "user_rights": {
        "name": "Deletion & User Rights",
        "keywords": [
            "delete your data",
            "delete your account",
            "deletion",
            "right to access",
            "right to delete",
            "right to object",
            "access your information",
            "correct your information",
        ],
    },
    "camera": {
        "name": "Camera Access",
        "keywords": [
            "camera access",
            "access your camera",
            "camera permission",
            "camera",
        ],
    },
    "microphone": {
        "name": "Microphone Access",
        "keywords": [
            "microphone access",
            "access your microphone",
            "microphone permission",
            "microphone",
        ],
    },
    "security": {
        "name": "Security & Encryption",
        "keywords": [
            "encryption",
            "encrypted",
            "security measures",
            "security safeguards",
            "protect your information",
            "data security",
            "secure your data",
        ],
    },
    "consent": {
        "name": "Consent",
        "keywords": [
            "your consent",
            "with your consent",
            "consent to",
            "you agree",
            "by using this service",
            "permission",
        ],
    },
    "personalized_advertising": {
        "name": "Personalized Advertising",
        "keywords": [
            "personalized advertising",
            "personalised advertising",
            "targeted advertising",
            "interest-based advertising",
            "behavioral advertising",
            "advertising partners",
        ],
    },
    "children": {
        "name": "Children's Data",
        "keywords": [
            "children's data",
            "children's information",
            "under 13",
            "under 16",
            "children",
            "child",
            "minors",
        ],
    },
}


def _longest_matches(keywords: list[str], text: str) -> list[str]:
    lowered = text.lower()

    found = [
        keyword
        for keyword in keywords
        if keyword.lower() in lowered
    ]

    found.sort(
        key=lambda keyword: len(keyword),
        reverse=True,
    )

    selected = []

    for keyword in found:
        keyword_lower = keyword.lower()

        if any(
            keyword_lower in selected_keyword.lower()
            for selected_keyword in selected
        ):
            continue

        selected.append(keyword)

    return selected


def detect_clauses(text: str) -> list[dict]:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned = re.sub(r"\s+", " ", text).strip()
    lowered = cleaned.lower()

    if not lowered:
        return []

    findings = []

    for category, config in CLAUSE_CATEGORIES.items():
        matches = _longest_matches(
            config["keywords"],
            cleaned,
        )

        if matches:
            findings.append(
                {
                    "category": category,
                    "name": config["name"],
                    "matches": matches,
                    "match_count": len(matches),
                }
            )

    return findings

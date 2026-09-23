CATEGORY_PRECEDENCE = [
    "children",
    "user_rights",
    "retention",
    "third_party_sharing",
    "location",
    "tracking",
    "camera",
    "microphone",
    "security",
    "personalized_advertising",
    "consent",
    "personal_data",
]


def get_category_priority(category: str) -> int:
    try:
        return CATEGORY_PRECEDENCE.index(category)
    except ValueError:
        return len(CATEGORY_PRECEDENCE)

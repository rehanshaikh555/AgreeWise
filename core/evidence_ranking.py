from core.category_precedence import get_category_priority
from core.category_relevance import CATEGORY_PRIMARY_PHRASES


# These are generic categories where a more specific category
# should take ownership of overlapping evidence.
EXCLUSIVE_GENERIC_CATEGORIES = {
    "personal_data",
}


def get_sentence_category_matches(
    sentence: str,
    detected_categories: list[str],
) -> list[dict]:
    lowered = sentence.lower()
    matches = []

    for category in detected_categories:
        phrases = CATEGORY_PRIMARY_PHRASES.get(category, [])

        matched_phrases = [
            phrase
            for phrase in phrases
            if phrase.lower() in lowered
        ]

        if matched_phrases:
            matches.append(
                {
                    "category": category,
                    "phrases": matched_phrases,
                    "priority": get_category_priority(category),
                }
            )

    return sorted(
        matches,
        key=lambda item: (
            item["priority"],
            -len(item["phrases"]),
        ),
    )


def should_include_category(
    category: str,
    sentence_matches: list[dict],
) -> bool:
    if not sentence_matches:
        return False

    current = next(
        (
            item
            for item in sentence_matches
            if item["category"] == category
        ),
        None,
    )

    if current is None:
        return False

    # Only suppress generic categories when a more specific
    # category also claims the same sentence.
    if category not in EXCLUSIVE_GENERIC_CATEGORIES:
        return True

    best = sentence_matches[0]

    return best["category"] == category

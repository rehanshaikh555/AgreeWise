from core.category_relevance import CATEGORY_PRIMARY_PHRASES
from core.clause_detector import detect_clauses
from core.context_analyzer import analyze_context
from core.document_metadata import analyze_metadata
from core.document_type_detector import detect_document_type
from core.evidence_extractor import extract_evidence
from core.evidence_ranking import (
    get_sentence_category_matches,
    should_include_category,
)
from core.language_detector import detect_language


def analyze_document(text: str) -> dict:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned_text = text.strip()

    if not cleaned_text:
        return {
            "status": "empty",
            "language": {
                "code": "unknown",
                "name": "Unknown",
                "confidence": 0.0,
            },
            "metadata": analyze_metadata(""),
            "document_type": {
                "type": "unknown",
                "name": "Unknown",
                "confidence": 0.0,
                "matches": [],
            },
            "findings": [],
        }

    language = detect_language(cleaned_text)
    metadata = analyze_metadata(cleaned_text)
    document_type = detect_document_type(cleaned_text)
    clauses = detect_clauses(cleaned_text)

    detected_categories = [
        clause["category"]
        for clause in clauses
    ]

    findings = []

    for clause in clauses:
        evidence_items = extract_evidence(
            cleaned_text,
            clause["matches"],
            CATEGORY_PRIMARY_PHRASES.get(
                clause["category"],
                [],
            ),
        )

        enriched_evidence = []

        for evidence in evidence_items:
            sentence = evidence["sentence"]

            sentence_matches = get_sentence_category_matches(
                sentence,
                detected_categories,
            )

            if not should_include_category(
                clause["category"],
                sentence_matches,
            ):
                continue

            context = analyze_context(sentence)

            enriched_evidence.append(
                {
                    "sentence": sentence,
                    "matches": evidence["matches"],
                    "context": context["context"],
                    "context_label": context["label"],
                    "context_indicators": context["indicators"],
                }
            )

        findings.append(
            {
                "category": clause["category"],
                "name": clause["name"],
                "matches": clause["matches"],
                "match_count": clause["match_count"],
                "evidence": enriched_evidence,
            }
        )

    return {
        "status": "complete",
        "language": language,
        "metadata": metadata,
        "document_type": document_type,
        "findings": findings,
    }

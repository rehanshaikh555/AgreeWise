from pathlib import Path

from core.analyzer import analyze_document


SAMPLE_POLICY = Path(
    "tests/data/sample_privacy_policy.txt"
).read_text(encoding="utf-8")


def get_finding(result: dict, category: str) -> dict:
    return next(
        finding
        for finding in result["findings"]
        if finding["category"] == category
    )


def test_analyzer_detects_document_type_and_language():
    result = analyze_document(SAMPLE_POLICY)

    assert result["status"] == "complete"
    assert result["document_type"]["type"] == "privacy_policy"
    assert result["language"]["code"] == "en"


def test_analyzer_detects_core_categories():
    result = analyze_document(SAMPLE_POLICY)

    expected_categories = {
        "personal_data",
        "location",
        "tracking",
        "third_party_sharing",
        "retention",
        "user_rights",
        "camera",
        "microphone",
        "security",
        "consent",
        "personalized_advertising",
        "children",
    }

    detected_categories = {
        finding["category"]
        for finding in result["findings"]
        if finding["evidence"]
    }

    assert expected_categories <= detected_categories


def test_camera_and_microphone_share_evidence():
    result = analyze_document(SAMPLE_POLICY)

    camera = get_finding(result, "camera")
    microphone = get_finding(result, "microphone")

    assert camera["evidence"]
    assert microphone["evidence"]

    camera_sentence = camera["evidence"][0]["sentence"]
    microphone_sentence = microphone["evidence"][0]["sentence"]

    assert camera_sentence == microphone_sentence
    assert "camera" in camera_sentence.lower()
    assert "microphone" in microphone_sentence.lower()


def test_consent_can_share_evidence_with_other_categories():
    result = analyze_document(SAMPLE_POLICY)

    consent = get_finding(result, "consent")

    assert len(consent["evidence"]) >= 2

    sentences = [
        item["sentence"].lower()
        for item in consent["evidence"]
    ]

    assert any("camera" in sentence for sentence in sentences)
    assert any("privacy policy" in sentence for sentence in sentences)


def test_children_evidence_is_not_generic_personal_data():
    result = analyze_document(SAMPLE_POLICY)

    children = get_finding(result, "children")
    personal = get_finding(result, "personal_data")

    assert children["evidence"]

    assert any(
        "children under 13" in item["sentence"].lower()
        for item in children["evidence"]
    )

    assert not any(
        "children under 13" in item["sentence"].lower()
        for item in personal["evidence"]
    )


def test_personal_data_collection_is_preserved():
    result = analyze_document(SAMPLE_POLICY)

    personal = get_finding(result, "personal_data")

    assert len(personal["evidence"]) == 1

    sentence = personal["evidence"][0]["sentence"].lower()

    assert "we collect information" in sentence
    assert "email address" in sentence
    assert "phone number" in sentence

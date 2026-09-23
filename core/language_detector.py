from langdetect import DetectorFactory, detect_langs

DetectorFactory.seed = 0


LANGUAGE_NAMES = {
    "en": "English",
    "hi": "Hindi",
    "mr": "Marathi",
    "gu": "Gujarati",
    "bn": "Bengali",
    "ta": "Tamil",
    "te": "Telugu",
    "kn": "Kannada",
    "ml": "Malayalam",
    "pa": "Punjabi",
    "ur": "Urdu",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-cn": "Chinese",
}


def detect_language(text: str) -> dict:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned = " ".join(text.split())

    if len(cleaned) < 20:
        return {
            "code": "unknown",
            "name": "Unknown",
            "confidence": 0.0,
        }

    try:
        results = detect_langs(cleaned)

        if not results:
            return {
                "code": "unknown",
                "name": "Unknown",
                "confidence": 0.0,
            }

        result = results[0]
        code = result.lang
        confidence = float(result.prob)

        return {
            "code": code,
            "name": LANGUAGE_NAMES.get(code, code.upper()),
            "confidence": round(confidence, 4),
        }

    except Exception:
        return {
            "code": "unknown",
            "name": "Unknown",
            "confidence": 0.0,
        }

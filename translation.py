def to_hindi(text: str) -> str:
    replacements = {
        "leadership": "नेतृत्व",
        "warmth": "सहानुभूति",
        "spontaneity": "स्वतंत्रता",
        "overthinking": "अधिक सोच",
        "Be kind to yourself today.": "आज अपने प्रति दयालु रहें।",
    }
    for en, hi in replacements.items():
        text = text.replace(en, hi)
    return "[HI] " + text

def translate_if_needed(response: dict, lang: str) -> dict:
    if lang and lang.lower().startswith("hi"):
        response = response.copy()
        response["insight"] = to_hindi(response["insight"])
        response["language"] = "hi"
    return response

from datetime import datetime
from zodiac import infer_zodiac

ZODIAC_TEMPLATES = {
    "Aries": "Today, {name}, your energetic spirit helps you start new things — lean into quick decisions but avoid impulsive spending.",
    "Taurus": "{name}, your steady nature keeps a project on track today. Treat yourself gently and double-check financial choices.",
    "Gemini": "Curiosity leads you to new connections today, {name}. Use conversation to clarify an ongoing misunderstanding.",
    "Cancer": "{name}, focus on home and self-care today. Small domestic wins will boost your confidence.",
    "Leo": "Your innate leadership and warmth will shine today, {name}. Embrace spontaneity and avoid overthinking.",
    "Virgo": "{name}, attention to detail is your superpower today — tidy up loose ends and you'll reduce future stress.",
    "Libra": "Seek balance today, {name}. A small compromise at work can open a door socially.",
    "Scorpio": "Your intensity is an asset today, {name}. Channel it into creative work rather than confrontation.",
    "Sagittarius": "Adventure calls, {name}. Consider learning something new — a short course or book can pay off.",
    "Capricorn": "{name}, steady progress wins today. Focus on one measurable goal and celebrate the small milestone.",
    "Aquarius": "Innovative ideas find an audience today, {name}. Share one bold idea with a trusted friend.",
    "Pisces": "Creativity and empathy are highlighted for you today, {name}. Put a small idea into motion.",
}

def pseudo_llm_generate(user: dict) -> dict:
    sign = user.get("zodiac") or infer_zodiac(user["birth_date"])
    name = user.get("name", "")
    template = ZODIAC_TEMPLATES.get(sign, ZODIAC_TEMPLATES["Capricorn"])
    affectionate = name[-1].lower() in "aeiou" if name else False
    insight = template.format(name=name)
    if affectionate:
        insight += " Be kind to yourself today."
    return {
        "zodiac": sign,
        "insight": insight,
        "language": "en",
        "score": 0.6,
        "generated_at": datetime.utcnow().isoformat() + "Z",
    }

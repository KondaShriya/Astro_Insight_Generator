from datetime import datetime
from dateutil import parser

ZODIAC_DATES = [
    ("Capricorn", (12, 22), (1, 19)),
    ("Aquarius", (1, 20), (2, 18)),
    ("Pisces", (2, 19), (3, 20)),
    ("Aries", (3, 21), (4, 19)),
    ("Taurus", (4, 20), (5, 20)),
    ("Gemini", (5, 21), (6, 20)),
    ("Cancer", (6, 21), (7, 22)),
    ("Leo", (7, 23), (8, 22)),
    ("Virgo", (8, 23), (9, 22)),
    ("Libra", (9, 23), (10, 22)),
    ("Scorpio", (10, 23), (11, 21)),
    ("Sagittarius", (11, 22), (12, 21)),
]

def infer_zodiac(birth_date_str: str) -> str:
    dt = parser.isoparse(birth_date_str)
    month, day = dt.month, dt.day
    for sign, (sm, sd), (em, ed) in ZODIAC_DATES:
        if sm == em:
            if month == sm and sd <= day <= ed:
                return sign
        else:
            if (month == sm and day >= sd) or (month == em and day <= ed):
                return sign
    return "Capricorn"

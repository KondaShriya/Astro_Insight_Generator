from pydantic import BaseModel, ValidationError
from typing import Optional

class PredictInput(BaseModel):
    name: str
    birth_date: str
    birth_time: Optional[str] = None
    birth_place: Optional[str] = None
    language: Optional[str] = "en"

def safe_parse_input(payload: dict) -> PredictInput:
    try:
        return PredictInput(**payload)
    except ValidationError as e:
        raise ValueError(str(e))

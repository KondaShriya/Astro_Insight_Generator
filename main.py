from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uvicorn

from utils import safe_parse_input
from llm_stub import pseudo_llm_generate
from zodiac import infer_zodiac
from cache import SimpleTTLCache
from translation import translate_if_needed
from vector_store_stub import MockVectorStore

app = FastAPI(title="AstroInsight")

cache = SimpleTTLCache(ttl_seconds=600)
vector_store = MockVectorStore()

@app.post("/predict")
async def predict(payload: dict):
    try:
        inp = safe_parse_input(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    cache_key = f"insight:{inp.name}:{inp.birth_date}:{inp.language}"
    cached = cache.get(cache_key)
    if cached:
        return JSONResponse(content={"cached": True, **cached})

    zodiac = infer_zodiac(inp.birth_date)
    user = dict(name=inp.name, birth_date=inp.birth_date, birth_time=inp.birth_time or "", birth_place=inp.birth_place or "", zodiac=zodiac)

    retrieved = vector_store.retrieve(inp.name + " " + (inp.birth_place or ""), top_k=1)
    response = pseudo_llm_generate(user)
    response = translate_if_needed(response, inp.language)
    response["retrieved_context"] = retrieved

    cache.set(cache_key, response)
    return JSONResponse(content={"cached": False, **response})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

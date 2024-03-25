from fastapi import FastAPI, HTTPException, Security, status
from postal.parser import parse_address
from app.libs.auth import get_api_key

app = FastAPI(
    title="Postal Web Service",
    version="1.0",
    description="Simple web service for parsing address strings",
)


@app.post("/parse_address")
async def parse_address(address: str, api_key: str = Security(get_api_key)):
    parsed = {k: v for (v, k) in parses_address(address)}
    return {"status": "ok", "address": parsed}


if __name__ == "__main__":
    uvicorn.run(app)

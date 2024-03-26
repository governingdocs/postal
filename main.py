from fastapi import FastAPI, HTTPException, Security, status
from postal.parser import parse_address
from app.libs.auth import get_api_key
from pydantic import BaseModel

app = FastAPI(
    title="Postal Web Service",
    version="1.0",
    description="Simple web service for parsing address strings",
)


class Address(BaseModel):
    address: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/parse_address")
async def main(address: Address, api_key: str = Security(get_api_key)):
    parsed = {k: v for (v, k) in parse_address(address.address)}
    return {"status": "ok", "address": parsed}


if __name__ == "__main__":
    uvicorn.run(app)

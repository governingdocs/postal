from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader
import os


postal_api_key = os.environ.get("POSTAL_API_KEY", "")
api_key_header = APIKeyHeader(name="X-API-Key")


def get_api_key(api_key_header: str = Security(api_key_header)) -> str:
    if api_key_header == postal_api_key:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )

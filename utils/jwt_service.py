from datetime import datetime, timedelta
import jwt
from fastapi import HTTPException, status
from dotenv import load_dotenv
import os

load_dotenv()


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24


SECRET = os.getenv("SECRET")


def create_access_token(data: dict):
    to_encode = data.copy()

    # Convert ObjectId to string representation if present
    if 'id' in to_encode:
        to_encode['id'] = str(to_encode['id'])

    expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_token(token: str) -> dict:
    """Verify JWT token"""
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )


def verify_google_token(token_id, client_id):
    """Verify Google OAuth token"""
    from google.oauth2 import id_token
    from google.auth.transport import requests

    google_request = requests.Request()

    try:
        payload = id_token.verify_oauth2_token(
            token_id, google_request, client_id
        )

        if payload["aud"] != client_id:
            raise HTTPException(status_code=401, detail="Unauthorized")

        return payload
    except Exception as e:
        print(f"Google token verification error: {e}")
        raise HTTPException(status_code=401, detail="Invalid Google token")

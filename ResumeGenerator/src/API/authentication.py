from typing import TypedDict

import google.oauth2.id_token
from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from google.auth.transport import requests

firebase_request_adapter = requests.Request()


async def authenticate_with_token(id_token: str):

    if not id_token:
        raise ValueError("No token provided")

    try:
        claims = google.oauth2.id_token.verify_firebase_token(
            id_token, firebase_request_adapter
        )
    except ValueError as exc:
        raise ValueError("Unauthorized") from exc
    return claims


class AuthClaims(TypedDict):
    name: str
    iss: str
    aud: str
    auth_time: int
    user_id: str
    sub: str
    iat: int
    exp: int
    email: str
    email_verified: bool
    firebase: dict[str, dict]


class FirebaseOAuthBearer(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)
        self.claims: AuthClaims = None
        self.id_token: str = None

    async def __call__(self, request: Request):
        credentials = await super().__call__(request)
        if not credentials:
            raise HTTPException(status_code=401, detail="No token provided")
        try:
            self.id_token = credentials.credentials
            self.claims = await authenticate_with_token(credentials.credentials)
        except ValueError as exc:
            raise HTTPException(status_code=401, detail="Unauthorized") from exc

        return self.claims

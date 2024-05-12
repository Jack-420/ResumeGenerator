from typing import Annotated

import google.oauth2.id_token
from fastapi import Depends, HTTPException, status

from .constants import firebase_request_adapter, oauth2_scheme
from .models import AuthClaims


async def authenticate_with_token(
    id_token: Annotated[str, Depends(oauth2_scheme)]
) -> AuthClaims:

    if not id_token:
        raise ValueError("No token provided")

    try:
        claims = google.oauth2.id_token.verify_firebase_token(
            id_token, firebase_request_adapter
        )
    except ValueError as exc:
        raise ValueError("Unauthorized") from exc
    return AuthClaims(**claims)


async def get_current_user(
    claims: Annotated[AuthClaims, Depends(authenticate_with_token)]
) -> AuthClaims:
    if not claims:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return claims

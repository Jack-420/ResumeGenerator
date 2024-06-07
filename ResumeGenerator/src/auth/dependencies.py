from typing import Annotated

import google.oauth2.id_token
from fastapi import Depends, HTTPException, status
from firebase_admin import auth
from firebase_admin.auth import UserRecord

from ..firebase import app
from .constants import firebase_request_adapter, oauth2_scheme
from .models import AuthClaims


async def authenticate_with_token(
    id_token: Annotated[str, Depends(oauth2_scheme)]
) -> AuthClaims:

    if not id_token:
        raise ValueError("No token provided")

    try:
        # TODO: verify with firebase_admin.auth.verify_id_token
        x = auth.verify_id_token(id_token, app)
        print(f"Verified token: {x}")
        print(f"Verified token type: {type(x)}")

        claims = google.oauth2.id_token.verify_firebase_token(
            id_token, firebase_request_adapter
        )
    except ValueError as exc:
        raise ValueError("Unauthorized") from exc
    return AuthClaims(**claims)


async def get_current_user(
    claims: Annotated[AuthClaims, Depends(authenticate_with_token)]
) -> UserRecord:
    if not claims:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # TODO: get user from firebase_admin.auth.get_user so change var name to user in all the dependencies
    return auth.get_user(claims.user_id)

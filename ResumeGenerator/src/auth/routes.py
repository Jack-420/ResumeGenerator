from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from .services import sign_in_with_email_and_password

router = APIRouter()


@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    sign_in_response = sign_in_with_email_and_password(
        form_data.username, form_data.password
    )
    return {"access_token": sign_in_response.idToken, "token_type": "bearer"}

from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.templating import Jinja2Templates

from ..authentication import AuthClaims, FirebaseOAuthBearer, authenticate_with_token

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, "templates")))

token_auth_scheme = FirebaseOAuthBearer()

router = APIRouter()


@router.get("/")
async def authenticate(request: Request):
    id_token = request.cookies.get("token")

    if not id_token:
        raise HTTPException(status_code=401, detail="No token provided")

    try:
        claims = await authenticate_with_token(id_token)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail="Unauthorized") from exc

    return claims


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    claims = None
    error_message = None

    id_token = request.cookies.get("token", "")

    try:
        claims = await authenticate_with_token(id_token)
    except ValueError as exc:
        error_message = str(exc)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "user_data": claims,
            "error_message": error_message,
            "token": request.cookies.get("token"),
        },
    )


@router.get("/private")
def private(claims: Annotated[AuthClaims, Depends(token_auth_scheme)]):

    return {"message": "You are authorized to access this route"}

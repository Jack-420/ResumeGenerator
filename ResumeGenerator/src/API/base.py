from pathlib import Path

import google.oauth2.id_token
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from google.auth.transport import requests

firebase_request_adapter = requests.Request()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, "templates")))

router = APIRouter()


# @router.get("/")
async def authenticate_with_token(request: Request):
    id_token = request.cookies.get("token")

    if not id_token:
        raise ValueError("No token provided")

    return google.oauth2.id_token.verify_firebase_token(
        id_token, firebase_request_adapter
    )


@router.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    claims = None
    error_message = None

    try:
        claims = await authenticate_with_token(request)
    except ValueError as exc:
        error_message = str(exc)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "user_data": claims,
            "error_message": error_message,
        },
    )

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from ..authentication import authenticate_with_token
from . import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
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

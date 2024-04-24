from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from firebase_admin import auth

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/login/google")
# async def google_login():
#     # Redirect user to Google Sign-In flow with appropriate scopes
#     # (e.g., email, profile) and state parameter (for CSRF protection)
#     return {
#         "url": f"https://accounts.google.com/o/oauth2/v2/auth?"
#         f"client_id={YOUR_CLIENT_ID}"
#         f"&redirect_uri={YOUR_REDIRECT_URI}"
#         f"&scope=openid profile email"
#         f"&response_type=code"
#         f"&state={YOUR_STATE_PARAM}"
#         f"&access_type=offline"  # Optional for refresh tokens
#     }

# templates = Jinja2Templates(directory="templates")


# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse(
#         request=request, name="index.html", context={"id": id}
#     )

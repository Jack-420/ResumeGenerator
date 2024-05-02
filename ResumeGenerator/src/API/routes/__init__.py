from pathlib import Path

from fastapi.templating import Jinja2Templates

from ..authentication import FirebaseOAuthBearer

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, "templates")))
token_auth_scheme = FirebaseOAuthBearer()

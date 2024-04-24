import firebase_admin
from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from firebase_admin import credentials
from pydantic import BaseModel

from .base import router as base_router
from .data import router as data_router
from .resume import router as resume_router

cred = credentials.Certificate(
    "resumegenerator-6a627-firebase-adminsdk-62uz7-77d8182b2e.json"
)
firebase_admin.initialize_app(cred)


# Define model for user data (optional)
class User(BaseModel):
    uid: str
    email: str | None = None
    name: str | None = None


# Dependency for getting currently authenticated user (optional)
# async def get_current_user(
#     token: str = Depends(Security(OAuth2PasswordBearer(tokenUrl=None))),
#     firebase=firebase_admin,
# ):
#     try:
#         decoded_token = firebase.auth().verify_id_token(token)
#         return User(**decoded_token)
#     except ValueError:
#         raise HTTPException(
#             status_code=401, detail="Invalid authentication credentials"
#         )


app = FastAPI()
app.include_router(base_router)
app.include_router(data_router)
app.include_router(resume_router)

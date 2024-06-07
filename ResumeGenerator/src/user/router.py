from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from firebase_admin import auth
from firebase_admin.auth import UserRecord

from ..auth.dependencies import get_current_user
from ..user.models import User
from .models import User
from .services import create_new_user, get_user_data, remove_user, update_user

router = APIRouter(
    prefix="/user", tags=["user"], responses={404: {"description": "Not found"}}
)


@router.get("/me")
def me(user: Annotated[User, Depends(get_current_user)]):
    print(user)
    x: UserRecord = auth.get_user(user.uid)
    print(dir(x))
    for attr in dir(x):
        if attr.startswith("_"):
            continue
        print(f"{attr} = {getattr(x, attr)}")
    print(type(x))


@router.get("/")
def user_data(user: Annotated[User, Depends(get_current_user)]) -> User:
    try:
        return User(**get_user_data(user.uid))
    except (KeyError, ValueError) as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(
    user: Annotated[User, Depends(get_current_user)], user_data: User
) -> User:
    try:
        return User(**create_new_user(user.uid, user_data))
    except KeyError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc


@router.patch("/", status_code=status.HTTP_200_OK)
def update_user_data(
    user: Annotated[User, Depends(get_current_user)], user_data: User
) -> User:
    try:
        return User(**update_user(user.uid, user_data))
    except KeyError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc


@router.delete("/", status_code=status.HTTP_200_OK)
def remove_user_data(
    user: Annotated[User, Depends(get_current_user)], user_data: User
) -> dict[str, str]:
    try:
        return {"message": remove_user(user.ui)}
    except KeyError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc

from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from google.protobuf.timestamp_pb2 import Timestamp

from ...core.models import ResumeData
from ..authentication import AuthClaims
from ..database import (
    delete_resume,
    get_all_resume,
    get_resume,
    save_resume,
    update_resume,
)
from . import token_auth_scheme

data: ResumeData = ResumeData.read_from_file(
    Path("ResumeGenerator/example/inputs/example_resume_data.json")
)

router = APIRouter(
    prefix="/data",
    tags=["data"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_all_resumes(
    auth_claims: Annotated[AuthClaims, Depends(token_auth_scheme)]
) -> list[str]:
    try:
        data = get_all_resume(auth_claims["user_id"])
    except KeyError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Resume not found"
        ) from exc

    if len(data) == 0:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, detail="No resumes found"
        )

    return data


@router.get("/{resume_name}")
async def read_resume_by_name(
    resume_name: str,
    auth_claims: Annotated[AuthClaims, Depends(token_auth_scheme)],
) -> ResumeData:
    try:
        data = get_resume(auth_claims["user_id"], resume_name)
    except (KeyError, ValueError) as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc
    return ResumeData(**data)


@router.post("/{resume_name}", status_code=status.HTTP_201_CREATED)
async def create_new_resume_by_name(
    resume_name: str,
    auth_claims: Annotated[AuthClaims, Depends(token_auth_scheme)],
    resume_data: ResumeData,
) -> ResumeData:
    try:
        saved_data = save_resume(
            auth_claims["user_id"], resume_name, resume_data.model_dump()
        )
    except KeyError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc

    if not saved_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Resume not found"
        )

    return ResumeData(**saved_data)


@router.patch("/{resume_name}", status_code=status.HTTP_200_OK)
async def update_resume_by_name(
    resume_name: str,
    auth_claims: Annotated[AuthClaims, Depends(token_auth_scheme)],
    resume_data: ResumeData,
) -> ResumeData:
    try:
        patched_data = update_resume(
            auth_claims["user_id"], resume_name, resume_data.model_dump()
        )
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

    if not patched_data:
        raise HTTPException(status_code=404, detail="Resume not found")

    return ResumeData(**patched_data)


@router.delete("/{resume_name}", status_code=status.HTTP_200_OK)
async def remove_resume_by_name(
    resume_name: str,
    auth_claims: Annotated[AuthClaims, Depends(token_auth_scheme)],
) -> dict[str, str]:
    try:
        time = delete_resume(auth_claims["user_id"], resume_name)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

    return {"deleted_at": str(time)}

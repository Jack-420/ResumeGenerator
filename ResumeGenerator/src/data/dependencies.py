from typing import Annotated

from fastapi import Depends, HTTPException, status

from ..auth.dependencies import get_current_user
from ..auth.models import AuthClaims
from .models import ResumeData
from .services import (
    read_all_resume,
    read_resume,
    remove_resume,
    save_resume,
    update_resume,
)


def get_all_resume(
    auth_claims: Annotated[AuthClaims, Depends(get_current_user)]
) -> list[str]:
    try:
        data = read_all_resume(auth_claims.user_id)
    except KeyError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Resume not found"
        ) from exc

    if len(data) == 0:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, detail="No resumes found"
        )

    return data


def get_resume(
    resume_name: str,
    auth_claims: Annotated[AuthClaims, Depends(get_current_user)],
) -> ResumeData:
    try:
        data = read_resume(auth_claims.user_id, resume_name)
    except (KeyError, ValueError) as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc

    return ResumeData(**data)


def post_resume(
    resume_name: str,
    auth_claims: Annotated[AuthClaims, Depends(get_current_user)],
    resume_data: ResumeData,
) -> ResumeData:
    try:
        saved_data = save_resume(
            auth_claims.user_id, resume_name, resume_data.model_dump()
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


def patch_resume(
    resume_name: str,
    auth_claims: Annotated[AuthClaims, Depends(get_current_user)],
    resume_data: ResumeData,
) -> ResumeData:
    try:
        patched_data = update_resume(
            auth_claims.user_id, resume_name, resume_data.model_dump()
        )
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

    if not patched_data:
        raise HTTPException(status_code=404, detail="Resume not found")

    return ResumeData(**patched_data)


def delete_resume(
    resume_name: str,
    auth_claims: Annotated[AuthClaims, Depends(get_current_user)],
) -> str:
    try:
        time = remove_resume(auth_claims.user_id, resume_name)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

    return time

from pathlib import Path

from fastapi import APIRouter, HTTPException, Request

from ..core.models import (
    Achievement,
    ContactInfo,
    Education,
    Experience,
    PersonalInfo,
    Project,
    ResumeData,
    Skill,
)
from .base import authenticate_with_token
from .database import get_all_resume, save_resume

data: ResumeData = ResumeData.read_from_file(
    Path("ResumeGenerator/example/inputs/example_resume_data.json")
)

router = APIRouter(
    prefix="/data",
    tags=["data"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_resume(request: Request) -> ResumeData:
    try:
        claims = await authenticate_with_token(request)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail="Unauthorized") from exc

    try:
        data = get_all_resume(claims["user_id"])
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Resume not found") from exc

    return data


@router.post("/")
async def create_base_resume(request: Request, resume_data: ResumeData):
    try:
        claims = await authenticate_with_token(request)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail="Unauthorized") from exc
    save_resume(claims["user_id"], resume_data.model_dump())


@router.get("/personal_info")
def read_personal_info() -> PersonalInfo:
    return data.personal_info


@router.get("/personal_info/contact_infos")
def read_contact_infos() -> list[ContactInfo]:
    return data.personal_info.contact_infos


@router.get("/educations")
def read_educations() -> list[Education]:
    return data.educations


@router.get("/skills")
def read_skills() -> list[Skill]:
    return data.skills


@router.get("/experience")
def read_experience() -> list[Experience]:
    return data.experience


@router.get("/projects")
def read_projects() -> list[Project]:
    return data.projects


@router.get("/achievements")
def read_achievements() -> list[Achievement]:
    return data.achievements

from pathlib import Path

from fastapi import APIRouter

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

data: ResumeData = ResumeData.read_from_file(
    Path("ResumeGenerator/example/inputs/example_resume_data.json")
)

router = APIRouter(
    prefix="/data",
    tags=["data"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def read_resume() -> ResumeData:
    return data


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

from pathlib import Path

from ...api import app
from ..data import (
    Achievement,
    ContactInfo,
    Education,
    Experience,
    PersonalInfo,
    Project,
    ResumeData,
    Skill,
)

data: ResumeData = ResumeData.load_data(
    Path("ResumeGenerator/example/inputs/example_resume_data.json")
)


@app.get("/resume/data")
def read_resume() -> ResumeData:
    return data


@app.get("/resume/data/personal_info")
def read_personal_info() -> PersonalInfo:
    return data.personal_info


@app.get("/resume/data/personal_info/contact_infos")
def read_contact_infos() -> list[ContactInfo]:
    return data.personal_info.contact_infos


@app.get("/resume/data/educations")
def read_educations() -> list[Education]:
    return data.educations


@app.get("/resume/data/skills")
def read_skills() -> list[Skill]:
    return data.skills


@app.get("/resume/data/experience")
def read_experience() -> list[Experience]:
    return data.experience


@app.get("/resume/data/projects")
def read_projects() -> list[Project]:
    return data.projects


@app.get("/resume/data/achievements")
def read_achievements() -> list[Achievement]:
    return data.achievements

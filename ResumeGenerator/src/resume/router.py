from typing import KeysView

from fastapi import APIRouter

from ..resume.resume_templates import ResumeTemplate

router = APIRouter(
    prefix="/resumes",
    tags=["resume"],
    responses={404: {"description": "Not found"}},
)


@router.get("/formats")
def read_formats() -> list[str]:
    return ResumeTemplate.available_templates()


# @app.get("/formats/{format_name}/preview")
# def read_preview(format_name: str) -> dict:
#     return {"format_name": format_name}

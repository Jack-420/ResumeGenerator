from typing import KeysView

from ...api import app
from ..resume_templates import ResumeTemplate


@app.get("/formats")
def read_formats() -> KeysView[str]:
    return ResumeTemplate.__members__.keys()


# @app.get("/formats/{format_name}/preview")
# def read_preview(format_name: str) -> dict:
#     return {"format_name": format_name}

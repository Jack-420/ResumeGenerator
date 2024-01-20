from pylatex import Document, NoEscape

from ..data import ResumeData
from .latex_body import (
    add_achievements,
    add_educations,
    add_expirence,
    add_projects,
    add_skills,
)
from .latex_headers import Header, set_resume_header


def load_preamble(doc: Document) -> None:
    with open("src/static/preamble.tex", "r", encoding="utf-8") as file:
        doc.preamble.append(NoEscape(file.read()))


def create_document(data: ResumeData) -> Document:
    latex = Document(documentclass="article", document_options=["letterpaper", "11pt"])

    load_preamble(latex)

    set_resume_header(latex, data.personal_info, Header.PHOTO_ON_LEFT)

    add_educations(latex, data.educations)
    add_skills(latex, data.skills)
    add_expirence(latex, data.experience)
    add_projects(latex, data.projects)
    add_achievements(latex, data.achievements)

    return latex

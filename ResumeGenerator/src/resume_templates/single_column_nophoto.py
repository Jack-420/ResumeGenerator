from pylatex import (
    Command,
    Document,
    FlushLeft,
    FlushRight,
    HorizontalSpace,
    NoEscape,
    Tabular,
    VerticalSpace,
)

from ..data import PersonalInfo, ResumeData
from .__single_column_content import (
    add_achievements,
    add_educations,
    add_expirence,
    add_projects,
    add_skills,
)


def set_resume_header(doc: Document, data: PersonalInfo):
    doc.append(NoEscape(r"% % -------------------- HEADING --------------------"))

    doc.append(
        NoEscape(
            rf"""
\begin{{flushright}}
\end{{flushright}}

\begin{{center}}
    \textbf{{\Huge \scshape {data.name}}} \\ \vspace{{8pt}}
    \small """
        )
    )

    doc.append(
        NoEscape(
            " $ $\n".join(
                rf"\faIcon{{{contact.fa_icon}}} \href{{{contact.link}}}{{\underline{{{contact.display}}}}}"
                for contact in data.contact_infos
            )
        )
    )

    doc.append(NoEscape(r"\end{center}"))


def create_document(data: ResumeData) -> Document:
    latex = Document(documentclass="article", document_options=["letterpaper", "11pt"])

    with open(
        "ResumeGenerator/src/resume_templates/single_column_nophoto_preamble.tex",
        "r",
        encoding="utf-8",
    ) as file:
        latex.preamble.append(NoEscape(file.read()))

    set_resume_header(latex, data.personal_info)

    add_educations(latex, data.educations)
    add_skills(latex, data.skills)
    add_expirence(latex, data.experience)
    add_projects(latex, data.projects)
    add_achievements(latex, data.achievements)

    return latex

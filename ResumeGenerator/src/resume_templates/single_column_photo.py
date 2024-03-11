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

    with doc.create(FlushLeft()):
        doc.append(HorizontalSpace("0.5cm"))
        doc.append(
            Command(
                "includegraphics",
                arguments=[data.photo],
                options="height=4cm",
            )
        )

    doc.append(NoEscape(r"\vspace{-150pt}"))

    with doc.create(FlushRight()):
        doc.append(
            Command(
                "textbf",
                arguments=[NoEscape(rf"\Huge {data.name}  \\ \vspace{{8pt}}")],
            )
        )

        with doc.create(Tabular("ll")):
            doc.append(VerticalSpace("6pt"))
            doc.append(
                NoEscape(
                    " \\\\ \\vspace{8pt}\n".join(
                        rf"\faIcon{{{contact.fa_icon}}} & \href{{{contact.link}}}{{\underline{{{contact.display}}}}}"
                        for contact in data.contact_infos
                    )
                )
            )
            doc.append(VerticalSpace("6pt"))


def create_document(data: ResumeData) -> Document:
    latex = Document(documentclass="article", document_options=["letterpaper", "11pt"])

    with open(
        "ResumeGenerator/src/formats/single_column_photo_preamble.tex",
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

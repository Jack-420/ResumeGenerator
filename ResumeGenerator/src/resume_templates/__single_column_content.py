from typing import List

from pylatex import Command, Document, NoEscape, Section, VerticalSpace

from ..data import Achievement, Education, Experience, Project, Skill


def add_educations(doc: Document, educations: List[Education]) -> None:
    doc.append(NoEscape(r"% % -------------------- EDUCATION --------------------"))

    doc.append(Section("Education"))

    doc.append(Command("resumeSubHeadingListStart"))

    for i, edu in enumerate(educations, start=1):
        doc.append(
            Command(
                "resumeSubheading",
                arguments=[
                    rf"{edu.institute}",
                    edu.year,
                    edu.degree,
                    f"{edu.marks.type}: {edu.marks.value}",
                ],
            )
        )

        if i != len(educations):
            doc.append(VerticalSpace("4pt"))

    doc.append(Command("resumeSubHeadingListEnd"))


def add_skills(doc: Document, skills: List[Skill]) -> None:
    doc.append(NoEscape(r"% % -------------------- SKILLS --------------------"))

    doc.append(Section("Skills"))

    doc.append(NoEscape(r"\begin{itemize}[leftmargin=0.15in, label={}]"))

    doc.append(
        Command(
            "small",
            arguments=[
                Command(
                    "item",
                    arguments=[
                        NoEscape(
                            "\n".join(
                                [
                                    rf"\textbf{{{skill.type}}}{{{': ' + ', '.join(skill.values)}}} \\"
                                    for skill in skills
                                ]
                            )
                        )
                    ],
                )
            ],
        )
    )

    doc.append(Command("end", arguments=["itemize"]))


def add_expirence(doc: Document, exps: List[Experience]):
    doc.append(NoEscape(r"%% -------------------- EXPERIENCE --------------------"))
    doc.append(Section("Professional Experience"))

    doc.append(Command("resumeSubHeadingListStart"))

    for exp in exps:
        doc.append(
            Command(
                r"resumeProjectHeading",
                arguments=[
                    NoEscape(
                        rf"\textbf{'{'}\href{{{exp.link}}}{'{'}\underline{{{exp.organization+'}'}}}}}"
                        + " $|$ "
                        + rf"\footnotesize\emph{{{exp.position}}}\vspace{{8pt}}{'}'}{{{exp.date}}}"
                        + "\\\\\n".join(
                            rf"{{\small{{{dec}}}}}" for dec in exp.descriptions
                        )
                        + "\\\\\n"
                        + rf"{{\small{{{', '.join(exp.technologies)}}}"
                    )
                ],
            )
        )

    doc.append(Command("resumeSubHeadingListEnd"))


def add_projects(doc: Document, projects: List[Project]):
    doc.append(NoEscape(r"%% -------------------- PROJECTS --------------------"))
    doc.append(Section("Projects"))
    doc.append(Command("resumeSubHeadingListStart"))

    for proj in projects:
        doc.append(Command("resumeProjectHeading"))
        doc.append(
            NoEscape(
                r"{\textbf{\href{"
                + str(proj.link)
                + r"}{\underline{"
                + proj.name
                + r"System}}} $|$ \footnotesize\emph{"
                + ", ".join(proj.technologies)
                + r"}}{}"
            )
        )
        doc.append(Command("resumeItemListStart"))
        doc.append(Command("resumeItem", arguments=[proj.description]))
        doc.append(Command("resumeItemListEnd"))

    doc.append(Command("resumeSubHeadingListEnd"))


def add_achievements(doc: Document, achievements: List[Achievement]):
    doc.append(NoEscape(r"%% -------------------- ACHIEVEMENTS --------------------"))
    doc.append(Section("Achievements"))
    doc.append(Command("resumeSubHeadingListStart"))

    for achiev in achievements:
        doc.append(Command("resumeProjectHeading"))
        doc.append(
            NoEscape(
                # {\textbf{Patent} $|$ \footnotesize\emph{Drain Clogging Prevention System}}{Application no. :202211017463}
                r"{\textbf{"
                + achiev.type
                + r"} $|$ \footnotesize\emph{"
                + achiev.title
                + r"}}{"
                + achiev.data
                + "}"
            )
        )

    doc.append(Command("resumeSubHeadingListEnd"))

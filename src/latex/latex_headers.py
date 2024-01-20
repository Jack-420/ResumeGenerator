from enum import Enum
from typing import List

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

from ..data import ContactInfo, PersonalInfo


class Header(Enum):
    PHOTO_ON_LEFT = 0
    PHOTO_ON_RIGHT = 1
    NO_PHOTO = 2


def set_resume_header(doc: Document, data: PersonalInfo, header_type: Header):
    doc.append(NoEscape(r"% % -------------------- HEADING --------------------"))

    if header_type is Header.PHOTO_ON_LEFT:
        return __set_left_photo_header(doc, data)
    elif header_type is Header.PHOTO_ON_RIGHT:
        return __set_right_photo_header(doc, data)
    elif header_type is Header.NO_PHOTO:
        return __set_no_photo_header(doc, data)
    else:
        raise ValueError("Invalid header_type!")


def __create_contact_info(contact_infos: List[ContactInfo]):
    contact_rows = [
        rf"\faIcon{{{contact.fa_icon}}} & \href{{{contact.link}}}{{\underline{{{contact.display}}}}} \\ \vspace{{8pt}}"
        for contact in contact_infos
    ]
    return "\n".join(contact_rows)


def __set_left_photo_header(doc: Document, data: PersonalInfo):
    with doc.create(FlushLeft()):
        doc.append(HorizontalSpace("0.5cm"))
        doc.append(
            Command(
                "includegraphics",
                arguments=[data.photo],
                options="width=5cm",
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


def __set_right_photo_header(doc: Document, data: PersonalInfo):
    ...


def __set_no_photo_header(doc: Document, data: PersonalInfo):
    ...

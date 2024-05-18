from __future__ import annotations

from typing import Type

from pylatex import Document

from ...data.models import ResumeData
from ..models import ResumeTemplateMetadata
from . import single_column_content


class ResumeTemplate:
    __subclasses: dict[str, Type["ResumeTemplate"]] = {}

    metadata: ResumeTemplateMetadata

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls not in cls.__subclasses:
            cls.__subclasses[cls.__name__] = cls
        else:
            raise ValueError(f"Duplicate subclass {cls.__name__}")

    @classmethod
    def available_templates(cls) -> list[str]:
        return list(cls.__subclasses.keys())

    @classmethod
    def get_template_by_name(cls, name: str) -> type[ResumeTemplate]:
        try:
            return cls.__subclasses[name]
        except KeyError as err:
            raise ValueError(f"No template found with name {name}") from err

    @classmethod
    def template_exists(cls, name: str) -> bool:
        return name in cls.__subclasses

    @classmethod
    def get_template_metadata(cls, name: str) -> ResumeTemplateMetadata:
        try:
            template = cls.get_template_by_name(name)
        except ValueError as err:
            raise ValueError(f"No template found with name {name}") from err
        return template.metadata

    @classmethod
    def create_document(cls, data: ResumeData) -> Document: ...


class SingleColumnNoPhoto(ResumeTemplate):

    metadata = ResumeTemplateMetadata(
        display_name="Single Column (No Photo)",
        details="A simple black-and-white single column resume format with no photo. Best for those who want a clean and simple resume.",
        number_format_columns=1,
        includes_photo=False,
        headings=[
            "Name",
            "Contacts",
            "Education",
            "Experience",
            "Skills",
            "Projects",
            "Achievements",
        ],
    )

    @classmethod
    def create_document(cls, data: ResumeData) -> Document:
        return single_column_content.create_document_with_nophoto(data)


class SingleColumnPhoto(ResumeTemplate):

    metadata = ResumeTemplateMetadata(
        display_name="Single Column (With Photo)",
        details="A simple black-and-white single column resume format with a photo. Best for those who want a clean and simple resume.",
        number_format_columns=1,
        includes_photo=True,
        headings=[
            "Name",
            "Contacts",
            "Education",
            "Experience",
            "Skills",
            "Projects",
            "Achievements",
        ],
    )

    @classmethod
    def create_document(cls, data: ResumeData) -> Document:
        return single_column_content.create_document_with_photo(data)

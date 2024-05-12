from typing import Type

from pylatex import Document

from ..models import ResumeData
from . import single_column_content


class ResumeTemplate:
    __subclasses: dict[str, Type["ResumeTemplate"]] = {}

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
    def get_template_by_name(cls, name: str):
        try:
            return cls.__subclasses[name]
        except KeyError as err:
            raise ValueError(f"No template found with name {name}") from err

    @classmethod
    def create_document(cls, data: ResumeData) -> Document: ...


class SingleColumnNoPhoto(ResumeTemplate):
    @classmethod
    def create_document(cls, data: ResumeData) -> Document:
        return single_column_content.create_document_with_nophoto(data)


class SingleColumnPhoto(ResumeTemplate):
    @classmethod
    def create_document(cls, data: ResumeData) -> Document:
        return single_column_content.create_document_with_photo(data)

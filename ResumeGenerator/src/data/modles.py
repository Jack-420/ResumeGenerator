from __future__ import annotations

import json
from pathlib import Path
from typing import List, Optional, Union

from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber

from .utils import AbsoluteFilePath, AnyUrlStr


class ContactInfo(BaseModel):
    type: str
    display: str
    link: Union[AnyUrlStr, EmailStr, PhoneNumber]
    fa_icon: str


class Address(BaseModel):
    line1: str
    line2: Optional[str] = ""
    city: str
    state: str
    country: str
    pin_code: int


class PersonalInfo(BaseModel):
    name: str
    photo: AbsoluteFilePath
    address: Address
    contact_infos: List[ContactInfo]


class Marks(BaseModel):
    type: str
    value: float


class Education(BaseModel):
    institute: str
    degree: str
    status: str
    year: int
    marks: Marks


class Skill(BaseModel):
    type: str
    values: List[str]


class Experience(BaseModel):
    organization: str
    position: str
    date: str
    link: Optional[AnyUrlStr]
    descriptions: List[str]
    technologies: List[str]


class Project(BaseModel):
    name: str
    link: Optional[AnyUrlStr]
    technologies: List[str]
    description: str


class Achievement(BaseModel):
    type: str
    title: str
    data: str


class ResumeData(BaseModel):
    personal_info: PersonalInfo
    educations: List[Education]
    skills: List[Skill]
    experience: List[Experience]
    projects: List[Project]
    achievements: List[Achievement]

    @staticmethod
    def load_data(path: Path) -> ResumeData:
        with path.open("r", encoding="utf-8") as json_file:
            json_data: dict = json.load(json_file)
            return ResumeData(**json_data)

    def data_for_latex(self) -> ResumeData:
        data_dict = self.model_dump()
        self.__replace_hash_with_latex_hash(data_dict)
        return ResumeData(**data_dict)

    def __replace_hash_with_latex_hash(self, data: dict):
        for key, value in data.items():
            if isinstance(value, dict):
                self.__replace_hash_with_latex_hash(value)
            elif isinstance(value, list):
                if isinstance(value[0], str):
                    data[key] = [item.replace("#", "\\#") for item in value]
                for item in value:
                    if isinstance(item, dict):
                        self.__replace_hash_with_latex_hash(item)
            elif isinstance(value, str):
                data[key] = value.replace("#", "\\#")

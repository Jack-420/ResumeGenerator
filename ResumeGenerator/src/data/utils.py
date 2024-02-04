from pathlib import Path
from typing import Annotated

from pydantic import AnyUrl, BeforeValidator, TypeAdapter

AnyUrlTypeAdapter = TypeAdapter(AnyUrl)
AnyUrlStr = Annotated[
    str,
    BeforeValidator(lambda value: AnyUrlTypeAdapter.validate_python(value) and value),
]


def file_exists(value: str):
    file_path = Path(value)
    if not file_path.exists():
        raise ValueError(f"File {file_path} does not exist")
    return str(file_path.absolute())


AbsoluteFilePath = Annotated[
    str,
    BeforeValidator(file_exists),
]

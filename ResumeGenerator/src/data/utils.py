from typing import Annotated

from pydantic import AnyUrl, BeforeValidator, FilePath, TypeAdapter

AnyUrlTypeAdapter = TypeAdapter(AnyUrl)
AnyUrlStr = Annotated[
    str,
    BeforeValidator(lambda value: AnyUrlTypeAdapter.validate_python(value) and value),
]

AbsoluteFilePath = Annotated[
    FilePath,
    BeforeValidator(lambda value: FilePath(value).absolute()),
]

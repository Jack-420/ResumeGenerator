from typing import Annotated

from pydantic import AnyUrl, BeforeValidator, TypeAdapter

AnyUrlTypeAdapter = TypeAdapter(AnyUrl)
AnyUrlStr = Annotated[
    str,
    BeforeValidator(lambda value: AnyUrlTypeAdapter.validate_python(value) and value),
]

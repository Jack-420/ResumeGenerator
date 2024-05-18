from typing import Annotated

from firebase_admin import firestore
from pydantic import AnyUrl, BeforeValidator, TypeAdapter

from ..firebase import app
from .utils import file_exists

db = firestore.client(app)
users_collection = db.collection("users")

AnyUrlTypeAdapter = TypeAdapter(AnyUrl)
AnyUrlStr = Annotated[
    str,
    BeforeValidator(
        lambda value: (
            (AnyUrlTypeAdapter.validate_python(value) and value) if value else ""
        )
    ),
]

AbsoluteFilePath = Annotated[
    str,
    BeforeValidator(file_exists),
]

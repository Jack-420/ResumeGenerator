from typing import Annotated

from fastapi import Depends, UploadFile
from google.cloud.firestore_v1 import DocumentReference, DocumentSnapshot

from ..auth.dependencies import get_current_user
from ..auth.models import AuthClaims
from .constants import storage_bucket, users_collection
from .models import User


def get_user_data(user_id: str) -> dict:
    doc: DocumentSnapshot = users_collection.document(user_id).get()

    if not doc.exists:
        raise KeyError(f"User data for {user_id} not found")

    data = doc.to_dict()
    if not data:
        raise ValueError(f"User data for {user_id} has no data")
    return data


def create_new_user(
    user_id: str,
    user_data: User,
    profile_pic: UploadFile = None,
):
    doc_ref: DocumentReference = users_collection.document(user_id)
    doc: DocumentSnapshot = doc_ref.get()

    if doc.exists:
        raise KeyError(f"User data for {user_id} already exists")

    doc_ref.set(user_data.model_dump())

    data = doc_ref.get().to_dict()
    if not data:
        raise ValueError(f"User data for {user_id} has no data")
    return data


def update_user(
    user_id: str,
    user_data: User,
    profile_pic: UploadFile = None,
):
    doc_ref: DocumentReference = users_collection.document(user_id)
    doc: DocumentSnapshot = doc_ref.get()

    if not doc.exists:
        raise KeyError(f"User data for {user_id} not found")

    data = doc_ref.get().to_dict()
    if not data:
        raise ValueError(f"User data for {user_id} has no data")
    return data


def remove_user(user_id: str) -> str:
    doc_ref: DocumentReference = users_collection.document(user_id)
    doc: DocumentSnapshot = doc_ref.get()

    if not doc.exists:
        raise KeyError(f"User data for {user_id} not found")

    return str(doc_ref.delete())


def store_file(user_id: str, file_name: str, file: bytes, content_type: str) -> str:
    blob = storage_bucket.blob(f"{user_id}/{file_name}")
    blob.upload_from_file(file, content_type=content_type)
    return blob.public_url


def store_profile_pic(user_id: str, file: bytes) -> str:
    blob = storage_bucket.blob(f"profile_photo/{user_id}")
    blob.upload_from_file(file, content_type="image/jpeg")
    return blob.public_url


def get_file_url(user_id: str, file_name: str) -> str:
    blob = storage_bucket.blob(f"{user_id}/{file_name}")
    return blob.public_url


def get_profile_pic_url(user_id: str) -> str:
    blob = storage_bucket.blob(f"{user_id}/profile_photo/profile_pic")
    return blob.public_url

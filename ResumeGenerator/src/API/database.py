import firebase_admin
from firebase_admin import credentials, firestore

from ResumeGenerator.src.core.models import ResumeData

cred = credentials.Certificate(
    "resumegenerator-6a627-firebase-adminsdk-62uz7-77d8182b2e.json"
)
firebase_admin.initialize_app(cred)
db = firestore.client()
resume_collection = db.collection("resume")


def get_all_resume(user_id: str):
    doc = resume_collection.document(user_id).get()
    if not doc.exists:
        raise KeyError(f"User with id {user_id} not found")
    return ResumeData(**doc.to_dict())


def save_resume(user_id: str, resume: dict):
    resume_collection.document(user_id).set(resume)

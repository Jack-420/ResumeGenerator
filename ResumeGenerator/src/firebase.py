import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(
    "resumegenerator-6a627-firebase-adminsdk-62uz7-77d8182b2e.json"
)
firebase_admin.initialize_app(cred)

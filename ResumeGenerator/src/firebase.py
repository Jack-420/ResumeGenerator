import firebase_admin
from firebase_admin import credentials

from .config import SETTINGS

cred = credentials.Certificate(SETTINGS.serviceAccountCertificatePath)
app = firebase_admin.initialize_app(cred)

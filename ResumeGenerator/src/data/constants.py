from firebase_admin import firestore

from ..firebase import app

db = firestore.client(app)
users_collection = db.collection("users")

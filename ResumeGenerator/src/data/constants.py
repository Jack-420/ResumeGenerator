from firebase_admin import firestore

db = firestore.client()
users_collection = db.collection("users")

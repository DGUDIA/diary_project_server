import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("../config/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection(u'messages')
docs = users_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
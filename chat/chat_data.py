import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import sys
import os

# cred = credentials.Certificate("./serviceAccountKey.json")
# firebase_admin.initialize_app(cred)

# db = firestore.client()

# users_ref = db.collection(u'messages')
# docs = users_ref.stream()

# for doc in docs:
#     print(u'{} => {}'.format(doc.id, doc.to_dict()))


    
def send_diary():
    cred = credentials.Certificate("./serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    users_ref = db.collection(u'messages')
    docs = users_ref.stream()
    
    result = []
    for doc in docs:
        if doc.to_dict()['isMe'] == True:
            result.append(doc.to_dict()['diary'])
    return result

# print(send_diary())



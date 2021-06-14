import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import sys
import os
import time


# def to_fire_ans(diary, isMe, sender):
#     now = time.localtime()
#     cred = credentials.Certificate("./serviceAccountKey.json")
#     firebase_admin.initialize_app(cred)
#     db = firestore.client()
#     doc_ref = db.collection(u'messages')
#     doc_ref.add({
#         u'diary': str(diary),
#         u'isMe': bool(isMe),
#         u'sender': str(sender),
#         u'timestamp': "%04d/%02d/%02d %02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
#     })
    
    
def to_fire_answer(diary, isMe, sender, emotion, link):
    cred = credentials.Certificate("./serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    users_ref = db.collection("messages")
    print(users_ref)
    query = users_ref.order_by(u'timestamp')
    docs = query.stream()
    result = []
    for doc in docs:
        if doc.to_dict()['isMe'] == True and doc.to_dict()['sender'] == sender:
            result.append(doc.to_dict())
            
    final = result[-1]
        
    doc_ref = db.collection(u'messages')
    doc_ref.add({
        u'diary': str(diary),
        u'isMe': bool(isMe),
        u'sender': str(sender),
        u'timestamp': final['timestamp'],
        u'emotion': str(emotion),
        u'link': str(link)
    })
    return result
    
# to_fire_ans('안녕', 'true', 'izero3127@gmail.com')
print(to_fire_answer('안녕', False, 'izero3127@gmail.com', '기쁨', 'link'))
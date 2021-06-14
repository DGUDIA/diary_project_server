import Diary2

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import sys
import os


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
    
    
# dairy = send_diary()
print("문단을 입력해보세요")
para=input()
print("슬픔, 중립, 행복, 불안, 분노, 예외")
response = Diary2.predict(para)
if response[0] == 1:
    print(' "슬픔" 으로 예측 되었습니다.')
if response[1] == 1:
    print(' "중립" 으로 예측 되었습니다.')
if response[2] == 1:
    print(' "행복" 으로 예측 되었습니다.')
if response[3] == 1:
    print(' "불안" 으로 예측 되었습니다.')
if response[4] == 1:
    print(' "분노" 로 예측 되었습니다.')
if response[5] == 1:
    print(' "예외" 로 예측 되었습니다.')

# print(response)

# print(Diary2.predict("너무 슬퍼요"))

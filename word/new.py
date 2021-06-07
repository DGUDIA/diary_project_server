from konlpy.tag import Twitter
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
from collections import Counter
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
sender = 'izero3127@gmail.com'

kkma=Twitter()
# f=open("speech.txt",mode='r',encoding='utf-8')
# txt=f.read()
# f.close()

# print(speech)

db = firestore.client()

users_ref = db.collection("messages").order_by('createdOn')
docs = users_ref.stream()
result = ""
for doc in docs:
    if doc.to_dict()['isMe'] == True and doc.to_dict()['sender'] == sender:
        result += doc.to_dict()['diary']
speech=kkma.nouns(result)        
print(result)

#TFIDF
tfidf = TfidfVectorizer()
txt_matrix= tfidf.fit_transform(speech) #특성 행렬을 만든다.
word_id=defaultdict(lambda : 0)
for idx,feature in enumerate(tfidf.get_feature_names()): #단어 목록에 index(순서) 부여
    word_id[feature] = idx
print('----------------------------------------------------------')
print("출력")
print('----------------------------------------------------------')
speech_word=[]
for i, s in enumerate(speech):
    for token in s.split():
        if txt_matrix[i,word_id[token]]>0:# idf 값이 0인것은 제외한다.
            speech_word.append(token)
            print(((token,txt_matrix[i,word_id[token]]))) # 단어에 해당하는 idf 값을 출력하기 위함


import pytagcloud
speech_cnt={}
for word in speech_word:
    speech_cnt[word]=speech_cnt.get(word,0)+1
print(speech_cnt)


for key,value in list(speech_cnt.items()):
    if key=='것이' or key=='것은' or key=='하는' or key=='이를': # 2번 이상 등장하는 쓸모없는 어절 제거
        del speech_cnt[key]
cnt=Counter(speech_cnt)

n=cnt.most_common(50) # 상위 50개의 단어
print(n)
speech_wc=pytagcloud.make_tags(n,maxsize=80) # 워드 클라우드 생성
pytagcloud.create_tag_image(speech_wc,str(sender)+'.png',size=(1000,600),
                           fontname='We',rectangular=False
                          )

os.system('git add .')
os.system('git commit -m "picture auto"')
os.system('git push origin master')
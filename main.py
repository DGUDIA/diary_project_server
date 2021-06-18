from flask import Flask, redirect, url_for, request, render_template, make_response, session, escape, Response
import csv
import json
from datetime import datetime
from functools import wraps
import sys
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import sys
import os
import time
from pytz import timezone
from NLP import Diary2
from NLP import senti
from web.db import get_naver, get_twitter, get_insta
from jinja2 import Environment, FileSystemLoader
from flask import Flask, render_template, redirect, url_for
import shutil
import os
import datetime
from static import word_pic
from flask import send_file




fmt = "%Y-%m-%d %H:%M:%S %Z%z"
KST = datetime.datetime.now(timezone('Asia/Seoul'))
fmt = "%Y/%m/%d %H:%M:%S"
print(KST.strftime(fmt))


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

'''
def render_maker_anger(list_n, list_t, sender, sertime, diary =""):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('webpage.html')
    output = template.render(naver=list_n, twitter=list_t)
    filename = './templates/'+str(sender)+sertime+'.html'
    print(filename)
    with open(filename,'w', -1, 'utf-8') as fh:
        fh.write(output)
    
def render_maker_happy(list_n, list_t, sender, sertime, diary =""):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('webpage.html')
    output = template.render(naver=list_n, twitter=list_t)
    filename = './templates/'+str(sender)+sertime+'.html'
    print(filename)
    with open(filename,'w', -1, 'utf-8') as fh:
        fh.write(output)
def render_maker_sad(list_n, list_t, sender, sertime, diary =""):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('webpage.html')
    output = template.render(naver=list_n, twitter=list_t)
    filename = './templates/'+str(sender)+sertime+'.html'
    print(filename)
    with open(filename,'w', -1, 'utf-8') as fh:
        fh.write(output)
def render_maker_neutral(list_n, list_t, sender, sertime, diary =""):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('webpage.html')
    output = template.render(naver=list_n, twitter=list_t)
    filename = './templates/'+str(sender)+sertime+'.html'
    print(filename)
    with open(filename,'w', -1, 'utf-8') as fh:
        fh.write(output)
def render_maker_anxious(list_n, list_t, sender, sertime, diary =""):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('webpage.html')
    output = template.render(naver=list_n, twitter=list_t)
    filename = './templates/'+str(sender)+sertime+'.html'
    print(filename)
    with open(filename,'w', -1, 'utf-8') as fh:
        fh.write(output)
        '''


def render_maker(list_n, list_t, list_i, sender, sertime, diary =""):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('webpage.html')
    output = template.render(naver=list_n, twitter=list_t, insta=list_i)
    filename = './templates/'+str(sender)+sertime+'.html'
    print(filename)
    with open(filename,'w', -1, 'utf-8') as fh:
        fh.write(output)

@app.route('/show/<username>/<sertime>')
def show(username, sertime):
    filename = str(username) + sertime + '.html'
    return render_template(filename, sertime=sertime)

@app.route('/sad/<username>/<sertime>')
def sad_show(username, sertime):
    list_n = get_naver('슬픔')
    list_t = get_twitter('슬픔')
    list_i = get_insta('슬픔')
    render_maker(list_n=list_n, list_t=list_t, list_i=list_i, sender = username, sertime = sertime)
    return redirect(url_for('show', username=username, sertime=sertime))

@app.route('/neutral/<username>/<sertime>')
def neutral_show(username, sertime):
    list_n = get_naver('중립')
    list_t = get_twitter('중립')
    list_i = get_insta('중립')
    render_maker(list_n=list_n, list_t=list_t, list_i=list_i, sender = username, sertime = sertime)
    return redirect(url_for('show', username=username, sertime=sertime))

@app.route('/happy/<username>/<sertime>')
def happy_show(username, sertime):
    list_n = get_naver('행복')
    list_t = get_twitter('행복')
    list_i = get_insta('행복')
    render_maker(list_n=list_n, list_t=list_t, list_i=list_i, sender = username, sertime = sertime)
    return redirect(url_for('show', username=username, sertime=sertime))

@app.route('/anxious/<username>/<sertime>')
def anxious_show(username, sertime):
    list_n = get_naver('불안')
    list_t = get_twitter('불안')
    list_i = get_insta('불안')
    render_maker(list_n=list_n, list_t=list_t, list_i=list_i, sender = username, sertime = sertime)
    return redirect(url_for('show', username=username, sertime=sertime))

@app.route('/angry/<username>/<sertime>')
def angry_show(username, sertime):
    list_n = get_naver('분노')
    list_t = get_twitter('분노')
    list_i = get_insta('분노')
    render_maker(list_n=list_n, list_t=list_t, list_i=list_i, sender = username, sertime = sertime)
    return redirect(url_for('show', username=username, sertime=sertime))

# 나중에 옮길것 위에꺼


def as_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        res = f(*args, **kwargs)
        res = json.dumps(res, ensure_ascii=False).encode('utf8')
        return Response(res, content_type='application/json; charset=utf-8')
    return decorated_function


@app.route('/get_image', methods=['POST'])
def get_image():
    sender = request.form['email']
    word_pic.wordcloud_s(sender, total_diary(sender))
    return redirect(url_for('images'), sender=sender)


@app.route('/images/<sender>')
def get_images(sender):
    return render_template('word_cloud.html', sender = sender, filename = sender.replace('@','').replace('.',''))
   


    
    # filename = os.path.join(os.path.dirname(os.path.abspath(__file__)))+'/'+sender+'.jpg'
    # return send_file('./word/'+filename, mimetype='image/jpg')

@app.route('/')
def hello():
    return 'Hello'

# @app.route('/db', methods=['POST'])
# @as_json
# def getdb():
#     email = request.form['email']
#     return read_db(email)

@app.route('/send', methods=['POST'])
def receive():
    receive = request.form['text']
    print(receive)
    return receive
fmtt="%Y%MYd%H%M%S"
cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
@app.route('/chat', methods=['POST'])
def index():
    time = request.form['timestamp']
    diary = request.form['diary']
    email = request.form['email']
    print(email)
    final = to_fire_answer(diary, False, email, 'link')
    fire_calender(final, email)
    total_diary(email)
    return time, email
  

# 파이어 베이스 답변
def to_fire_answer(diary, isMe, sender, link):
    db = firestore.client()

    users_ref = db.collection("messages").order_by('createdOn')
    docs = users_ref.stream()
    result = []
    for doc in docs:
        if doc.to_dict()['isMe'] == True and doc.to_dict()['sender'] == sender:
            result.append(doc.to_dict())
            
    final = result[-1]
    
    
    emotion = sentence_sentiment(str(diary))
    emotion_dict = {'슬픔':0, '중립':1, '행복':2, '불안':3, '분노':4, '예외':5}
                                 
    if emotion == '슬픔':
        link = 'http://54.180.2.12:57349/sad/{0}/{1}'.format(sender, 1)
    elif emotion =='행복':
        link = 'http://54.180.2.12:57349/happy/{0}/{1}'.format(sender, 1)
    elif emotion =='분노':
        link = 'http://54.180.2.12:57349/angry/{0}/{1}'.format(sender, 1)
    elif emotion =='중립':
        link = 'http://54.180.2.12:57349/neutral/{0}/{1}'.format(sender, 1)
    else:
        link = 'http://54.180.2.12:57349/anxious/{0}/{1}'.format(sender, 1)
                                 
    doc_ref = db.collection(u'messages')
    doc_ref.add({
        u'diary': str(senti.sentence_picker(int(emotion_dict[emotion]))),
        u'isMe': bool(isMe),
        u'sender': str(sender),
        u'timestamp': str(KST.strftime(fmt)),
        u'createdOn': firestore.SERVER_TIMESTAMP,
        u'emotion': str(emotion),
        u'link': str(link)
    })

    return final

def fire_calender(final, email):
    db = firestore.client()
    doc2_ref = db.collection(u'answers')
    doc2_ref.add({
        u'diary': final['diary'],
        u'sender': str(email),
        u'timestamp': str(KST.strftime(fmt)),
        u'y': str(int(KST.strftime("%Y"))),
        u'm': str(int(KST.strftime("%m"))),
        u'd': str(int(KST.strftime("%d"))),
        u't': str(KST.strftime("%H:%M:%S")),
        u'createdOn': firestore.SERVER_TIMESTAMP,
        u'type': str(sentence_sentiment(final['diary']))
    })    
    
# 파이어 베이스 답변
def total_diary(sender):
    db = firestore.client()

    users_ref = db.collection("answers").order_by('createdOn')
    docs = users_ref.stream()
    result = []
    for doc in docs:
        if doc.to_dict()['sender'] == sender:
            result.append(doc.to_dict()['diary'])
            # result[doc.to_dict()['type']] += 1
    diary = ' '.join(result)
    
    data = {
        u'sender': str(sender),
        u'diary': diary,
    }
    e = u'{}'.format(sender)
    doc_ref = db.collection(u'total').document(e).set(data)
    return diary
    
@app.route('/words', methods=['POST'])
def words():
    sender = request.form['sender']
    word_pic.wordcloud_s(firestore.client(), sender, total_diary(sender))
    
# 감성분석
def sentence_sentiment(sentence):
    response = Diary2.predict(sentence)
    if response[0] == 1:
        return('슬픔')
    if response[1] == 1:
        return('중립')
    if response[2] == 1:
        return('행복')
    if response[3] == 1:
        return('불안')
    if response[4] == 1:
        return('분노')
    if response[5] == 1:
        return('예외')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    
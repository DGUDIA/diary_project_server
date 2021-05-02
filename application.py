from flask import Flask, redirect, url_for, request, render_template, make_response, session, escape
import pymysql
import csv
import datetime


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/db')
def db():
    return "db  DB"

@app.route('/send', methods=['POST'])
def receive():
    receive = request.form['text']
    print(receive)
    return receive

@app.route('/chat', methods=['POST'])
def index():
    email = request.form['email']
    # time = request.form['time']
    diary = request.form['diary']
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y년%m월%d일 %H시%M분%S초')
    print(email)
    print(diary)
    print(nowDatetime)
    f = open('./chat/db.csv','w', newline='')
    wr = csv.writer(f)
    wr.writerow([email, nowDatetime, diary])
    return nowDatetime

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    
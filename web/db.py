import sqlite3
import random
'''
def get_naver(feelings):
    conn = sqlite3.connect("naver.db", isolation_level=None)
    cur = conn.cursor()

    cur.execute("SELECT * FROM naver")

    #0~59 : 슬픔
    #60~74 : 중립
    #75~89 : 행복
    #90~134 : 불안
    #135~179 : 분노
    rows = cur.fetchall()
    conn.close()
    
    if feelings == '슬픔':
        naver_idx = random.sample(list(range(0, 60)), 10)
    elif feelings == '중립':
        naver_idx = random.sample(list(range(60, 75)), 10)
    elif feelings == '행복':
        naver_idx = random.sample(list(range(75, 105)), 10)
    elif feelings == '불안':
        naver_idx = random.sample(list(range(105, 150)), 10)
    elif feelings == '분노':
        naver_idx = random.sample(list(range(150, 195)), 10)
    else:
        return "감정을 분류하는데 실패했습니다."

    naver_list = []

    for i in range(0, 10):
        naver_dict = {}
        idx = naver_idx[i]
        row = rows[idx]

        naver_dict['postdate'] = row[3]
        naver_dict['title'] = row[1]
        naver_dict['content'] = row[0]
        naver_dict['link'] = row[2]
        naver_dict['keyword'] = row[4]
        naver_dict['feeling'] = row[5]
        naver_list.append(naver_dict)

    

    return naver_list


def get_twitter(feelings):
    conn = sqlite3.connect("twitter.db", isolation_level=None)
    cur = conn.cursor()

    cur.execute("SELECT * FROM twitterdb")

    rows = cur.fetchall()
    conn.close()
    if feelings == '슬픔':
        twit_idx = random.sample(list(range(0, 60)), 10)
    elif feelings == '중립':
        twit_idx = random.sample(list(range(60, 75)), 10)
    elif feelings == '행복':
        twit_idx = random.sample(list(range(75, 105)), 10)
    elif feelings == '불안':
        twit_idx = random.sample(list(range(105, 150)), 10)
    elif feelings == '분노':
        twit_idx = random.sample(list(range(150, 195)), 10)
    else:
        return "감정을 분류하는데 실패했습니다."

    twit_list = []
    
    for i in range(0, 10):
        twit_dict = {}
        idx = twit_idx[i]
        row = rows[idx]

        twit_dict['time'] = row[0]
        twit_dict['content'] = row[1]
        twit_dict['likey'] = row[2]
        twit_dict['retweet'] = row[3]
        twit_dict['keyword'] = row[4]
        twit_dict['feeling'] = row[5]
        twit_list.append(twit_dict)

    

    return twit_list
'''

def get_naver(feelings):
    conn = sqlite3.connect("naver.db", isolation_level=None)
    cur = conn.cursor()

    cur.execute("SELECT * FROM naver")

    #0~59 : 슬픔
    #60~74 : 중립
    #75~89 : 행복
    #90~134 : 불안
    #135~179 : 분노
    rows = cur.fetchall()

    if feelings == '슬픔':
        naver_idx = random.sample(list(range(0,60)), 10)
    elif feelings == '중립':
        naver_idx = random.sample(list(range(60, 75)), 10)
    elif feelings == '행복':
        naver_idx = random.sample(list(range(75, 90)), 10)
    elif feelings == '불안':
        naver_idx = random.sample(list(range(90, 135)), 10)
    elif feelings == '분노':
        naver_idx = random.sample(list(range(135, 180)), 10)
    else:
        return "감정을 분류하는데 실패했습니다."

    naver_list = []

    for i in range(0, 10):
        naver_dict = {}
        idx = naver_idx[i]
        row = rows[idx]

        naver_dict['postdate'] = row[3]
        naver_dict['title'] = row[1]
        naver_dict['content'] = row[0]
        naver_dict['link'] = row[2]
        naver_dict['keyword'] = row[4]
        naver_dict['feeling'] = row[5]
        naver_list.append(naver_dict)

    conn.close()

    return naver_list


def get_twitter(feelings):
    conn = sqlite3.connect("twitter.db", isolation_level=None)
    cur = conn.cursor()

    cur.execute("SELECT * FROM twitterdb")

    rows = cur.fetchall()
    conn.close()
    
    if feelings == '슬픔':
        twit_idx = random.sample(list(range(0, 60)), 10)
    elif feelings == '중립':
        twit_idx = random.sample(list(range(60, 75)), 10)
    elif feelings == '행복':
        twit_idx = random.sample(list(range(75, 90)), 10)
    elif feelings == '불안':
        twit_idx = random.sample(list(range(90, 135)), 10)
    elif feelings == '분노':
        twit_idx = random.sample(list(range(135, 180)), 10)
    else:
        return "감정을 분류하는데 실패했습니다."

    twit_list = []

    for i in range(0, 10):
        twit_dict = {}
        idx = twit_idx[i]
        row = rows[idx]

        twit_dict['time'] = row[0]
        twit_dict['content'] = row[1]
        twit_dict['likey'] = row[2]
        twit_dict['retweet'] = row[3]
        twit_dict['keyword'] = row[4]
        twit_dict['feeling'] = row[5]
        twit_list.append(twit_dict)

    

    return twit_list

def get_insta(feelings):
    conn = sqlite3.connect("instagram.db", isolation_level=None)
    cur = conn.cursor()

    cur.execute("SELECT * FROM instadb")

    rows = cur.fetchall()
    conn.close()
    # 너무 많이 게시물을 올리면 랙걸려서 6개로 함
    if feelings == '행복':
        insta_idx = random.sample(list(range(0, 10)), 5)
    elif feelings == '슬픔':
        insta_idx = random.sample(list(range(10, 20)), 5)
    elif feelings == '중립':
        insta_idx = random.sample(list(range(20, 30)), 5)
    elif feelings == '불안':
        insta_idx = random.sample(list(range(30, 40)), 5)
    elif feelings == '분노':
        insta_idx = random.sample(list(range(40, 50)), 5)

    insta_list = []

    for i in range(0, 5):
        insta_dict = {}
        idx = insta_idx[i]
        row = rows[idx]

        insta_list.append(row[1])

    

    return insta_list


kk = get_insta('슬픔')

print(kk)
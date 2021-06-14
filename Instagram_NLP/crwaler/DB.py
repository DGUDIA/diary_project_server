#데이터프레임 만들고 엑셀로 저장하기
import pandas as pd
import sqlite3


def make_df(results):
    results_df = pd.DataFrame(results)
    results_df.columns = ['content','data','like','place','tags']
    results_df.to_csv('./results/crawling_sample.csv', encoding="utf-8", index=False)

    
    conn = sqlite3.connect("insta.db", isolation_level=None)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS tables \
        (time datetime, id integer, content text, likey integer, retweet integer)")
    
    # 이전 테이블 내용 삭제
    conn.execute("DELETE from tables")

'''
conn = pymysql.connect(host='localhost', user='diary22', 
                       password='950205', charset='utf8') 


create table `crwaling`(
    `content` char(200) NOT NULL,
    `date` date NOT NULL,
    `tag` char(30) DEFAULT NULL
)
'''
import pymysql

def chat_to_mysql(email, time, diary):
    con = pymysql.connect(host='localhost', user ='izero', password='0000', db='diary', charset='utf8')
    cursor = con.cursor()
    # 삽입
    sql = """insert into chat (email, time, diary) values (%s, %s, %s)"""
    cursor.execute(sql, (str(email),str(time),str(diary)))
    con.commit()
    
    sql = "select * from chat where email = 'izero3127@gmail.com' order by time asc"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row_data in result:
        print(row_data[0])
        print(row_data[1])
        print(row_data[2])
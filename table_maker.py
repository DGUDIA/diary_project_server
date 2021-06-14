import pymysql

con = pymysql.connect(host='localhost', user ='izero', password='0000', db='diary', charset='utf8')
cursor = con.cursor()

sql = "ALTER table 'chat'"

cursor.execute(sql)
sql = "drop primary key"

cursor.execute(sql)
con.commit()

# # 삽입
# sql = "insert into chat (email, time, diary) values('test2','test','test')"
# cursor.execute(sql)
# con.commit()

# sql = "select * from chat"
# cursor.execute(sql)
# result = cursor.fetchall()
# for row_data in result:
# 	print(row_data[0])
# 	print(row_data[1])
# 	print(row_data[2])
import pymysql

def read_db(email):
    con = pymysql.connect(host='localhost', user ='izero', password='0000', db='diary', charset='utf8')
    cursor = con.cursor()
    
    sql = "select * from chat where email = %s order by time desc"
    cursor.execute(sql, email)
    result = cursor.fetchall()
    
    return_data = []
    for row_data in result:
        return_data.append({'email':row_data[0], 'time':row_data[1], 'diary':row_data[2]})
        print(row_data[2])
    return return_data
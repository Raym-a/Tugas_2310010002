import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='tugas_2310010002',
        cursorclass=pymysql.cursors.Cursor
    )
    conn.commit()
    conn.close()
import pymysql

HOST = '172.16.100.66'
PORT = 3306
USER = "root"
PASSWORD = "@)!&swd2NUC!*"
DB = "swd"

conn = pymysql.connect(host=HOST , user=USER, passwd=PASSWORD)

print(123)

cursor=conn.cursor()
cursor.execute("SELECT * from 2014batch;")
row=cursor.fetchone()
while(row is not None):
    print(row[0])
    row=cursor.fetchone()
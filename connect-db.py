#import pymysql

#HOST = '172.16.100.66'
#PORT = 3306
#USER = "root"
#PASSWORD = "@)!&swd2NUC!*"
#DB = "swd"

#conn = pymysql.connect(host=HOST , user=USER, passwd=PASSWORD, port=PORT)

#print(123)

#cursor=conn.cursor()
#cursor.execute("SELECT * from 2014batch;")
#row=cursor.fetchone()
#while(row is not None):
 #   print(row[0])
  #  row=cursor.fetchone()

import csv

f = open('studata.csv')
csv_f = csv.reader(f)

for row in csv_f:
 # print(row)
  print(row[0])
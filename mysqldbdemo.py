#!/usr/bin/env python

#extract zip file
#copy pymysql folder in C:\Users\MyUsername\AppData\Local\Programs\Python\Python35-32\Lib
#run the following code
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root123', db='test')



cur = conn.cursor()



print()
cur.execute("insert into product values(113, 'Marie gold', 'It Yummy', '2018-02-22',true,4)")
conn.commit()
cur.execute("SELECT * FROM product")
print(cur.description)
for row in cur:
    print(row[0],row[1])

cur.close()
conn.close()

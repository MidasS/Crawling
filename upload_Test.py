__author__ = '송동환'
import pymysql

db = pymysql.connect(host='114.108.167.124', port=3306, user='blue1028', passwd='gusdl57',charset ='utf8',db='blue1028')
c = db.cursor()

name_List=[17,'hi',55,'toto','sudo']

c.execute("INSERT INTO bymono VALUE(17,'hi',55,'toto','sudo')")


c.execute('select * from bymono')
rows = c.fetchall()

for r in rows:
    print(r)
    c.close()
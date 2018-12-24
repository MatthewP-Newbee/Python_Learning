#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Project: Python_Learning
# @Date: 2018/12/13
# @Author: MatthewP

import pymysql

db = pymysql.connect(host='localhost', user='root', password='C7355608', port=3306, db='spiders')
cursor = db.cursor()

sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count: ', cursor.rowcount)
    one = cursor.fetchone()
    print('One', one)
    results = cursor.fetchall()
    print('Results: ', results)
    print('Results Type: ', type(results))
    for row in results:
        print(row)
except:
    print('Error')
db.close()
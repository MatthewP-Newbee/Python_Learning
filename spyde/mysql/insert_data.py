#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Project: Python_Learning
# @Date: 2018/12/12
# @Author: MatthewP

import pymysql

id = '201800001'
user = 'BOB'
age = 'name'

db = pymysql.connect(host='localhost', user='root', password='C7355608', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()
db.close()
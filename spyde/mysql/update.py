#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Project: Python_Learning
# @Date: 2018/12/13
# @Author: MatthewP

import pymysql

db = pymysql.connect(host='localhost', user='root', password='C7355608', port=3306, db='spiders')
cursor = db.cursor()

data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 44
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                     values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
print(sql)
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Sucessful')
        db.commit()
except:
    print('Failed!')
    db.rollback()
db.close()
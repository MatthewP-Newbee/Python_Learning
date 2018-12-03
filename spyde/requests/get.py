#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author: MatthewP
# @Date: 12/3/2018
# @Email: matthewhakka@gmail.com

import requests

r = requests.get('https://www.baidu.com')
print(type(r))
print(type(r.text))
print(r.status_code)
print(r.text)
print(r.cookies)

data = {'name': 'germey', 'age': '22'}
r2 = requests.get('http://httpbin.org/get', params=data)
print(r2.text)
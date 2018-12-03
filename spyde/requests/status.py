#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author: MatthewP
# @Date: 12/3/2018
# @Email: matthewhakka@gmail.com

import requests

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

r = requests.get('http://www.jianshu.com', headers=head)
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)
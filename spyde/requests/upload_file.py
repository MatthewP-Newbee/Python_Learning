#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author: MatthewP
# @Date: 12/3/2018
# @Email: matthewhakka@gmail.com

import requests

files = {'file': open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)

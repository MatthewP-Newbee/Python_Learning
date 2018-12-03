#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author: MatthewP
# @Date: 12/3/2018
# @Email: matthewhakka@gmail.com

import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/1332434')
r = s.get('http://httpbin.org/cookies')
print(r.text)
#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author: MatthewP
# @Date: 11/30/2018
# @Email: matthewhakka@gmail.com

import http.cookiejar
import urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + '=' + item.value)
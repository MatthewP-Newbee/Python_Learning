#!/usr/bin/env python
# @Author: MatthewP
# @Date: 11/28/2018
# @Email: matthewhakka@gmail.com

from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Host': 'httpbin.org'
}
d = {'name': 'Germey'}
data = bytes(parse.urlencode(d), encoding='utf-8')
req = request.Request(url, data, headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
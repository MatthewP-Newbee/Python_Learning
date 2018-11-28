#!/usr/bin/env python
# @author: MatthewP
# @date: 11/28/2018
# @email: matthewhakka@gmail.com

import socket
import urllib.error
import urllib.parse
import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print('Object Type: {}'.format(type(response)))
print('Object status: {}'.format(response.status))
print('HTTP Response Headers: {}'.format(response.getheaders()))
print(response.read().decode('utf-8'))

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.001)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Time out')
    else:
        print(e)
        print('Other reason.')
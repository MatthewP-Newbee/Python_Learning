#!/usr/bin/env python
# @author: MatthewP
# @date: 11/28/2018
# @email: matthewhakka@gmail.com

import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print('Object Type: {}'.format(type(response)))
print('Object status: {}'.format(response.status))
print('HTTP Response Headers: {}'.format(response.getheaders()))
print(response.read().decode('utf-8'))
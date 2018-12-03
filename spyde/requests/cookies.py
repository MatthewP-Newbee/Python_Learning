#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author: MatthewP
# @Date: 12/3/2018
# @Email: matthewhakka@gmail.com

import requests

r = requests.get('https://github.com/requests/requests/')
for key, value in r.cookies.items():
    print(key + '=' + value)
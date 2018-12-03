#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author: MatthewP
# @Date: 12/3/2018
# @Email: matthewhakka@gmail.com

import requests

response = requests.get('https://www.12306.cn')
print(response.status_code)

response2 = requests.get('https://www.12306.cn', verify=False)
print(response2.status_code)
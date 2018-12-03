#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author: MatthewP
# @Date: 12/3/2018
# @Email: matthewhakka@gmail.com

import requests

head = {
    'cookie': '_zap=4c993177-8193-4ce6-abcc-d1675be0f78f; d_c0="AJDuqn0riQ2PThUD4qJ7bZ9ookGkl_h4pL8=|1525323614"; __utmz=51854390.1526460712.6.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _xsrf=KL0ewRyb7jMT6pj9GuXH87S8vG4MYFqB; q_c1=1090e14a254741d0b07f0d1cfbb495ca|1542687024000|1525236697000; r_cap_id="ZmY1YjQyYzNiNGI1NDM3MzkzNGJlMzRmMTVlNWM1NjE=|1542687024|3edb5459721b364088d9803cda9e851b2eec9a5a"; cap_id="ZWE4N2JlZjMzOTQ2NDBjYzlmN2U3YmQ2ZTc5MmU1MzA=|1542687024|99fc2be815ab648cd8ecaae9bac89e70cfe4c64d"; l_cap_id="MjdmNGI3NzQ2MTllNDU1NWFmMjY2MTBhNTNiMzU5Y2U=|1542687024|442098284dc85a85acc8488fac65296230f2a288"; capsion_ticket="2|1:0|10:1542687065|14:capsion_ticket|44:OWJjOTg2NmI1OWIyNDM4Mjk4MDIyOTFkNzIzODM3NDM=|c8d79454fa81fcce577916b6bf6679e1d0c137216c7ff4b3806253c9ba80e509"; z_c0="2|1:0|10:1542687072|4:z_c0|92:Mi4xNmdkd0JRQUFBQUFBa082cWZTdUpEU1lBQUFCZ0FsVk5ZTmZnWEFBZmwyU0RhTlpKQVRiam5Fay1MUnRleVRmYVVn|2a74749c4291a8b99dbb9463bc74b3cf67c6e15b5e9c14bdd36829cf0d7ec333"; __utmv=51854390.100--|2=registration_date=20170714=1^3=entry_date=20170714=1; tst=r; tgw_l7_route=156dfd931a77f9586c0da07030f2df36; __utma=51854390.789513267.1525236696.1543466422.1543827491.17; __utmb=51854390.0.10.1543827491; __utmc=51854390',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
r = requests.get('https://www.zhihu.com', headers=head)
print(r.text)
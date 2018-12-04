#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author: MatthewP
# @Date: 12/4/2018
# @Email: matthewhakka@gmail.com

import time
import re
import json
import requests


def one_page(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        return response.text
    else:
        print('Fetch nothing. URL: {}'.format(url))
        return None


def to_file(file, contents):
    pattern = re.compile('<dd>.*?board-index board-index.*?>(\d)</i>.*?<img data-src.*?(https.*?)".*?'
                         '<p class="name">.*?title="(.*?)".*?<p class="star">.*?主演：(.*?)</p>.*?class="releasetime">.*?上映时间：(.*?)</p>'
                         '.*?<i class="integer">(.*?)</i>.*?</dd>', re.S)
    items = pattern.findall(contents)
    for each in items:
        with open(file, 'a+') as fh:
            content = {'排名': each[0],
                       '海报图片': each[1],
                       '名称': each[2].strip(),
                       '主演': each[3].strip(),
                       '上映时间': each[4].strip(),
                       '评分': each[-1].strip()}
            json.dump(content, fh, ensure_ascii=False)


def main():
    for i in range(10):
        url = 'https://maoyan.com/board/4?offset=' + str(10*i)
        html = one_page(url)
        to_file('maoyan_top_100.txt', html)
        time.sleep(2)
        print('Fetching data...')
    print('Done!')

if __name__ == '__main__':
    main()
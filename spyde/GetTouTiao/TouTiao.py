#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Project: Python_Learning
# @Date: 2018/12/31
# @Author: MatthewP

import os
import requests
from urllib.parse import urlencode
from hashlib import md5


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'autoload': 'true',
        'keyword': '生物信息',
        'count': '20',
        'cur_tab': '1'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        respinse = requests.get(url)
        if respinse.status_code == 200:
            return respinse.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    data = json.get('data')
    if data:
        for item in data:
            title = item.get('title')
            images = item.get('image_list')
            if images:
                for image in images:
                    yield {
                        'image': 'https:' + image.get('url'),
                        'title': title
                    }


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{}/{}.{}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('File existed!')
    except requests.ConnectionError:
        print('Failed to save image.')


groups = [x * 20 for x in range(1, 6)]
for each in groups:
    page = get_page(each)
    for item in get_images(page):
        save_image(item)

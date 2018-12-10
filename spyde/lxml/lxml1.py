#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Project: Python_Learning
# @Date: 2018/12/10
# @Author: MatthewP

from lxml import etree

html = etree.parse('test.html', etree.HTMLParser())
result1 = html.xpath('//li[@class="item-0"]/a/text()')
print(result1)
result2 = html.xpath('//li[@class="item-0"]//text()')
print(result2)
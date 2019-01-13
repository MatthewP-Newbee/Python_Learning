#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Project: Python_Learning
# @Date: 2019/1/13
# @Author: MatthewP


class A(object):
    def __new__(cls):
        print('A.__new__')
        return 3

    def __init__(self):
        print('A.__init__')


A()
#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Project: Python_Learning
# @Date: 12/24/2018
# @Author: MatthewP

'''
Pool.apply_async() 可以作用于类，且用 get() 能获取到类实例。
'''

from multiprocessing import Pool
import random


class A(object):
    def __init__(self, num):
        self.num = num
        self.msg = self.get_msg()

    def get_msg(self):
        num = self.num + random.randint(1, 100)
        return num


if __name__ == '__main__':
    p = Pool()
    r = []
    for i in range(4):
        proc = p.apply_async(A, [3])
        r.append(proc)
    p.close()
    for each in r:
        rs = each.get(10)
        print(rs.get_msg())
        print(rs.msg)


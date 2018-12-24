#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Project: Python_Learning
# @Date: 12/24/2018
# @Author: MatthewP

from multiprocessing import Pool
from multiprocessing import Queue


class Test(object):
    def __init__(self, num):
        self.num = num


if __name__ == '__main__':
    p = Pool()
    q = Queue()
    for i in range(5):
        proc = p.apply_async(Test, args=(i,))
        q.put(proc)
    p.close()
    while not q.empty():
        q.get()
    p.join()


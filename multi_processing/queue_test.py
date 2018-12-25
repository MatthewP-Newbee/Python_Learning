#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Project: Python_Learning
# @Date: 12/24/2018
# @Author: MatthewP

'''
multiprocessing.Queue 使用 pickle 对对象进行序列化，但是 Pool.apply_async() 返回的 AsyncResult 对象无法被序列化，此时可以使用
queue.Queue
'''

from multiprocessing import Pool
import queue


class Test(object):
    def __init__(self, num):
        self.num = num


if __name__ == '__main__':
    p = Pool()
    q = queue.Queue()
    for i in range(5):
        proc = p.apply_async(Test, args=(i,))
        q.put(proc)
    p.close()
    while not q.empty():
        each = q.get()
        print(each.get().num)
    p.join()


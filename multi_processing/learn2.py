#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Project: Python_Learning
# @Date: 11/6/2018
# @Author: MatthewP

from multiprocessing import Process, Lock

def printer(item, lock):
    lock.acquire()
    try:
        print(item)
    finally:
        lock.release()

if __name__ == '__main__':
    lock = Lock()
    items = ['tango', 'foxtrot', 10]

    for item in items:
        p = Process(target=printer, args=(item, lock))
        p.start()
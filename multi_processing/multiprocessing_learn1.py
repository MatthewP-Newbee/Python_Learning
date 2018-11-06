#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Project: Python_Learning
# @Date: 11/6/2018
# @Author: MatthewP

import os
from multiprocessing import Process

def doubler(number):
    result = number*2
    proc = os.getpid()
    print('{} doubled to {} by process id: {}'.format(number, result, proc))

if __name__ == '__main__':
    numbers = [3, 43, 98, 22]
    procs = []

    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
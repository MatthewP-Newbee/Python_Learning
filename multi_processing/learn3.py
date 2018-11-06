#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Project: New_Health
# @Date: 11/6/2018
# @Author: MatthewP

from multiprocessing import Pool

def doubler(number):
    return number*2

if __name__ == '__main__':
    numbers = [5, 10, 20]
    pool = Pool(processes=3)
    print(pool.map(doubler, numbers))
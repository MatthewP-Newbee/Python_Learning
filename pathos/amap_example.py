#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Project: Python_Learning
# @Date: 19-3-10
# @Author: MatthewP

import time
from pathos.pp import ParallelPool
pool = ParallelPool(6)

results = pool.amap(pow, [1, 2, 3, 4], [5, 6, 7, 8])
while not results.ready():
    time.sleep(3)
    print('.', end=' ')

print(results.get())


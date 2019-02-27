#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Project: Python_Learning
# @Date: 2/27/2019
# @Author: MatthewP

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 4), columns=list('ABCD'),
                  index=pd.date_range('20130101', periods=5))
print(df)
print('----------------')
print(df.loc['20130102':'20130104'])
print(df.loc['20130104', 'B'])
print(df.A > 0)
print(df.loc[lambda df: df.A > 0, :])
print('****************')
print(df.iloc[1:3])
print(df.iloc[1, 1])

# 修改数值
s = pd.Series(np.random.randn(6), index=list('abcdef'))
print(s)
print('------------------')
s.loc['c':] = 0
print(s)

dfd = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=list('abc'))
print(dfd)
print(dfd.loc[dfd.index[[0, 2]], 'A'])
print(dfd.iloc[[0, 2], dfd.columns.get_loc('A')])
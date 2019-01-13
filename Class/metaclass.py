#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Project: Python_Learning
# @Date: 2019/1/13
# @Author: MatthewP

Foo = type('Foo', (object,), {'name': 'Darksouls'})
x = Foo()
print(x.name)
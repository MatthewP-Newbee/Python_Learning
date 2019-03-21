#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Project: Python_Learning
# @Date: 3/21/2019
# @Author: MatthewP

from dataclasses import dataclass
from typing import Any

@dataclass
class DataObject(object):
    name: str
    gender: str
    height: float = 160
    weight: float = 50
    age: Any = 13


test = DataObject("Matt", "Male")
print(test)
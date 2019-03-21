#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Project: Python_Learning
# @Date: 3/21/2019
# @Author: MatthewP

from dataclasses import make_dataclass, dataclass, field
from math import asin, cos, radians, sin, sqrt

# 自动包含 __init__(), __repr__(), __eq__()
Position = make_dataclass('Position', ['name', 'lat', 'lon'])

# 也可以定义函数
# frozen设定是否锁定属性值
@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = field(default=0.0, repr=False)

    def distance_to(self, other):
        r = 6371
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2) ** 2 + cos(phi_1) * cos(phi_2) *
             sin((lam_2 - lam_1) / 2) ** 2)
        return 2 * r * asin(sqrt(h))


oslo = Position('Oslo', 10.8, 59.9)
vancouver = Position('Vancouver', -123.1, 49.3)
print(oslo.distance_to(vancouver))


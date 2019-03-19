#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Project: Python_Learning
# @Date: 3/19/2019
# @Author: MatthewP

import datetime
from unittest.mock import Mock

tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    return 0 <= today.weekday() < 5


datetime.datetime.today.return_value = tuesday
assert is_weekday()

datetime.datetime.today.return_value = saturday
assert not is_weekday()



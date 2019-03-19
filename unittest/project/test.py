#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Project: Python_Learning
# @Date: 3/19/2019
# @Author: MatthewP

import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()

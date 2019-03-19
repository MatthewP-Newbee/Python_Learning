#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Project: Python_Learning
# @Date: 3/19/2019
# @Author: MatthewP

import unittest


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6)

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 7)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Project: Python_Learning
# @Date: 3/19/2019
# @Author: MatthewP


def capital_case(x: str):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Project: Python_Learning
# @Date: 3/19/2019
# @Author: MatthewP

import requests
import unittest
from unittest.mock import Mock

requests = Mock()


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


class TestCalendar(unittest.TestCase):
    def log_request(self, url):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {"12/25": "Christmas", '7/4': "Independence Day"}
        return response_mock

    def test_get_holidays_logging(self):
        requests.get.side_effect = self.log_request
        assert get_holidays()['12/25'] == 'Christmas'


if __name__ == '__main__':
    unittest.main()

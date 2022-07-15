#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/15 0015 14:36

import requests
import unittest
from common.common_api import CommonApi
from common.config_utils import read_config
from common.log_utils import log_pri

class GetAccessTokenCases(unittest.TestCase):
    def setUp(self) -> None:
        self.common_api=CommonApi()
        self.hosts=read_config.get_url

    def tearDown(self) -> None:
        pass

    def test_get_access_token(self):
        self._testMethodDoc='测试说明获取token成功'
        actual_result = self.common_api.get_access_token_api('client_credential',
                                                             read_config.get_appid,
                                                             read_config.get_secret)
        print(actual_result.json())
        self.assertEqual(actual_result.json()['expires_in'],7200)
        log_pri.info('获取token')

    def test_appid_error(self):
        self._testMethodDoc='测试说明当appid错误时的错误码与预期一致'
        actual_result = self.common_api.get_access_token_api('client_credential',
                                                             '123344',
                                                             read_config.get_secret)
        self.assertEqual(actual_result.json()['errcode'], 40013)
        log_pri.info('当appid错误时的错误码时')

if __name__ == '__main__':
    unittest.main()
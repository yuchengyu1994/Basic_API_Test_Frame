#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/15 0015 14:36

import requests
import unittest
from common.common_api import CommonApi
from common.config_utils import read_config
from common.log_utils import log_pri

class CreateTagCases(unittest.TestCase):
    def setUp(self) -> None:
        self.common_api = CommonApi()
        self.access_token=self.common_api.get_access_token()
        print(self.access_token)

    def tearDown(self) -> None:
        pass

    def test_add_tag(self):
        self._testMethodDoc='测试说明添加用户的标签'
        tag_json={   "tag" : {     "name" : "湖南"   } }
        print(self.access_token)
        actual_result=self.common_api.create_user_tag_api(self.access_token,tag_json).json()['tag']['name']
        self.assertEqual(actual_result,'湖南')
        log_pri.error('这个肯定会错，因为我没有取得接口权限，估计都走不到这里来，所以这句不会打印')


if __name__ == '__main__':
    unittest.main()
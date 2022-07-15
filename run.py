#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/15 0015 15:39
import os
import unittest

from common import HTMLTestReportCN
from common.config_utils import read_config


def get_all_cases_suite():
    test_suile = unittest.defaultTestLoader.discover(
        start_dir='./test_cases',
        pattern='*_cases.py',
        top_level_dir='./test_cases'
    )
    all_suite=unittest.TestSuite()
    all_suite.addTest(test_suile)
    return all_suite

def run_cases():
    current_path = os.path.dirname(__file__)
    report_path = os.path.join(current_path, read_config.get_report_path)
    report_dir=HTMLTestReportCN.ReportDirectory(report_path)
    report_dir.create_dir('APItest')
    report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
    fp =open(report_path,'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                             title='APItest',
                                             description='sxdsxs',
                                             tester='Yu')
    runner.run(get_all_cases_suite())
    fp.close()

if __name__ == '__main__':
    run_cases()
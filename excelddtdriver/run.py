# coding=utf-8
import unittest
from excelddtdriver.common import HTMLTestRunner_PY3 as HTMLTestRunner
# from excelddtdriver.common import HTMLTestRunner

import os
import datetime
from util.sendEmail import send_mail

curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "report")
print(report_path, "report_path")
if not os.path.exists(report_path): os.mkdir(report_path)
case_path = os.path.join(curpath, "case")


def add_case(casepath=case_path, rule="test*.py"):
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath,
                                                   pattern=rule, )
    return discover


def run_case(all_case, test_report=report_path):
    '''执行所有的用例, 并把结果写入测试报告'''
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    htmlreport = test_report + "\\" + now + "-result.html"
    print("测试报告生成地址：%s" % htmlreport)
    fp = open(htmlreport, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           verbosity=2,
                                           title="测试报告",
                                           description="用例执行情况")

    # 调用add_case函数返回值
    runner.run(all_case)

    fp.close()


def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))
    file_new = os.path.join(test_report, lists[-1])
    return file_new


if __name__ == "__main__":
    cases = add_case()
    run_case(cases)
    # send_mail(new_report(report_path))

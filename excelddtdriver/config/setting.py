#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'JingQi'
"""这里的数据主要是一些简单的配置信息"""
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
TEST_CONFIG = os.path.join(BASE_DIR, "database", "config.ini").replace("\\","/")
# 测试用例报告
TEST_REPORT = os.path.join(BASE_DIR, "report")




if __name__ == "__main__":
    print(BASE_DIR)
    print(TEST_CONFIG)

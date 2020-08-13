# coding:utf-8
import unittest
import ddt
import os
import requests
from excelddtdriver.common import base_api
from excelddtdriver.common import readExcel
from excelddtdriver.common import writeExcel

# 获取demo_api.xlsx路径
curpath = os.path.dirname(os.path.realpath(__file__))
# testxlsx = os.path.join(curpath, "invoice_data.xlsx")
testxlsx = os.path.join(curpath, "pro_data.xlsx")
# 复制demo_api.xlsx文件到report下

resultXlsx = os.path.join(os.path.join(os.path.dirname(curpath), "resultExcelDir"), "result.xlsx")
testdata = readExcel.ExcelUtil(testxlsx).dict_data()

"""
    用例
"""


@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        # 如果有登录的话，就在这里先登录了
        writeExcel.copy_excel(testxlsx, resultXlsx)  # 复制xlsx

    @ddt.data(*testdata)
    def test_api(self, data):
        # 先复制excel数据到report
        print("------------------------>", data)
        res = base_api.send_requests(data)
        base_api.wirte_result(res, filename=resultXlsx)
        # 检查点 checkpoint
        check = data["checkpoint"]
        print("检查点->：%s" % check)
        # 返回结果
        res_text = res["text"]
        print("返回实际结果->：%s" % res_text)
        # 断言
        self.assertTrue(check in res_text)


if __name__ == "__main__":
    unittest.main()

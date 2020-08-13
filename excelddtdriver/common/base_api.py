# coding:utf-8
"""
import json
import requests
from excelddtdriver.common.writeExcel import copy_excel, Write_excel
from util.VariableDemo import read
from util.VariableDemo import reverseData
from util.customLog import getLogger

session = requests.session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

logger = getLogger("D:\\file\\pWorkSpace\\excelddtdriver\\log\\")

# requests接口处理


def send_requests(testdata):
    dic = read(r"D:\file\pWorkSpace\excelddtdriver\case\demo_api.xlsx", "变量")
    '''封装requests请求'''

    method = testdata["method"]
    methodType = testdata["methodType"]
    url = testdata["url"]
    IsTheResultReused = testdata["IsTheResultReused"]  # 此请求的请响应结果是否被其他接口重用
    logger.info(str(method) + ":  " + str(url))
    # url后面的params参数
    try:
        params = eval(testdata["params"])
        # 做数据替换处理
        params = reverseData(params, dic)
        logger.info("参数:  " + str(params))
    except Exception as e:
        print(e, "错误提示")
        # logger.error("错误" + str(e))
        params = None
    test_nub = testdata['ID']
    print("*******正在执行用例：-----  %s  ----**********" % test_nub)
    print("请求方式：%s, 请求url:%s" % (method, url))
    print("请求params：%s" % params)

    # verify = False 禁用ssl
    if method == "post" and methodType == "dict":

        r = session.post(url, data=params, headers=headers, verify=False)
        print("headers -------------->", headers)
    elif method == "post" and methodType == "json":
        r = session.post(url, data=json.dumps(params), headers=headers, verify=False)
        # GET 请求拼接URL
    else:
        if len(str(params)) > 0:
            url += '?' + '&'.join([str(key) + '=' + str(value) for key, value in params.items()])
            logger.info("此时的请求方式为" + method + "此时的URL为 ： " + url)
            r = session.get(url, headers=headers, verify=False)

    if "token" in r.text:
        token = json.loads(r.text).get("res").get("token")
        headers["Authorization"] = token

    res = {"result": ""}  # 接受返回数据
    try:
        print("页面返回信息：%s" % r.text)
        res['ID'] = testdata['ID']
        res['rowNum'] = testdata['rowNum']
        res["statusCode"] = str(r.status_code)  # 状态码转成str
        res["text"] = r.text
        res["times"] = str(r.elapsed.total_seconds())  # 接口请求时间转str

        if res["statusCode"] != "200":
            res["error"] = res["text"]
        else:
            res["error"] = ""
        res["msg"] = ""
        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
            print("用例测试结果:   %s---->%s" % (test_nub, res["result"]))
        else:
            res["result"] = r.text
        return res
    # 捕获到异常的时候会写入Msg
    except Exception as msg:
        res["msg"] = str(msg)
        return res


def wirte_result(result, filename="result.xlsx"):
    # 返回结果的行数row_nub
    print(result)
    row_nub = result['rowNum']
    # statusCode
    wt = Write_excel(filename)
    wt.write(row_nub, 6, result['statusCode'])  # 写入返回状态码statusCode,第8列
    wt.write(row_nub, 7, result['times'])  # 耗时
    wt.write(row_nub, 8, result['error'])  # 状态码非200时的返回信息
    wt.write(row_nub, 10, result['result'])  # 测试结果 pass 还是fail
    wt.write(row_nub, 11, result['msg'])
    # 抛异常

# -------------------------当只有一个接口的结果会被引用----------------------------------


# coding:utf-8
import json
import requests
from excelddtdriver.common.writeExcel import copy_excel, Write_excel
from util.VariableDemo import read
from util.VariableDemo import reverseData
from util.customLog import getLogger

session = requests.session()

dictTheResultReused_t_003 = {}  # 字典数据被重用t_003

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 "
                  "Safari/537.36 "
}

logger = getLogger("D:\\file\\pWorkSpace\\excelddtdriver\\log\\")

# requests接口处理


def send_requests(testdata):
    dic = read(r"D:\file\pWorkSpace\excelddtdriver\case\demo_api.xlsx", "变量")
    '''封装requests请求'''

    method = testdata["method"]
    methodType = testdata["methodType"]
    url = testdata["url"]
    IsTheResultReused = testdata["IsTheResultReused"]  # 此请求的请响应结果是否被其他接口重用
    logger.info(str(method) + ":  " + str(url))
    # url后面的params参数
    try:
        params = eval(testdata["params"])
        # 做数据替换处理
        params = reverseData(params, dic)
        logger.info("参数:  " + str(params))
    except Exception as e:
        print(e, "错误提示")
        # logger.error("错误" + str(e))
        params = None
    test_nub = testdata['ID']
    print("*******正在执行用例：-----  %s  ----**********" % test_nub)
    print("请求方式：%s, 请求url:%s" % (method, url))
    print("请求params：%s" % params)

    return common_function(url, method, testdata, test_nub, methodType, params, IsTheResultReused, "companyIds", )


#　keyName,valueName
＃　需要替换的名和值


def common_function(url, method, testdata, test_nub, methodType, params, IsTheResultReused, keyName):
    global dictTheResultReused_t_003
    if len(dictTheResultReused_t_003) > 0:
        value = parse_dict(dictTheResultReused_t_003)

    print("params的类型=====>", type(params))
    if keyName in params.keys():
        params[keyName] = value
    if IsTheResultReused == 1:
        if method == "post" and methodType == "dict":
            r = session.post(url, data=params, headers=headers, verify=False)
            dictTheResultReused_t_003 = json.loads(r.text)
            print("headers -------------->", headers)
        elif method == "post" and methodType == "json":
            r = session.post(url, data=json.dumps(params), headers=headers, verify=False)
            dictTheResultReused_t_003 = json.loads(r.text)
        # GET 请求拼接URL
        else:
            if len(str(params)) > 0:
                url += '?' + '&'.join([str(key) + '=' + str(value) for key, value in params.items()])
                logger.info("此时的请求方式为" + method + "此时的URL为 ： " + url)
                r = session.get(url, headers=headers, verify=False)
                dictTheResultReused_t_003 = json.loads(r.text)
    else:
        if method == "post" and methodType == "dict":
            r = session.post(url, data=params, headers=headers, verify=False)
            print("替换后的参数为", params)
            print("headers -------------->", headers)
        elif method == "post" and methodType == "json":
            r = session.post(url, data=json.dumps(params), headers=headers, verify=False)

        # GET 请求拼接URL
        else:
            if len(str(params)) > 0:
                url += '?' + '&'.join([str(key) + '=' + str(value) for key, value in params.items()])
                logger.info("此时的请求方式为" + method + "此时的URL为 ： " + url)
                r = session.get(url, headers=headers, verify=False)

    if "token" in r.text:
        token = json.loads(r.text).get("res").get("token")
        headers["Authorization"] = token

    res = {"result": ""}  # 接受返回数据
    try:
        print("页面返回信息：%s" % r.text)
        res['ID'] = testdata['ID']
        res['rowNum'] = testdata['rowNum']
        res["statusCode"] = str(r.status_code)  # 状态码转成str
        res["text"] = r.text
        res["times"] = str(r.elapsed.total_seconds())  # 接口请求时间转str

        if res["statusCode"] != "200":
            res["error"] = res["text"]
        else:
            res["error"] = ""
        res["msg"] = ""
        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
            print("用例测试结果:   %s---->%s" % (test_nub, res["result"]))
        else:
            res["result"] = r.text
        return res
    # 捕获到异常的时候会写入Msg
    except Exception as msg:
        res["msg"] = str(msg)
        return res


# 针对接口解析需要复用的字典 返回一个需要的类型
def parse_dict(dic):
    l2_dict_003 = []
    l1 = dic.get("res").get("res")
    for i in l1:
        l2_dict_003.append(i.get("companyId"))
    return l2_dict_003


def wirte_result(result, filename="result.xlsx"):
    # 返回结果的行数row_nub
    print(result)
    row_nub = result['rowNum']
    # statusCode
    wt = Write_excel(filename)
    wt.write(row_nub, 6, result['statusCode'])  # 写入返回状态码statusCode,第8列
    wt.write(row_nub, 7, result['times'])  # 耗时
    wt.write(row_nub, 8, result['error'])  # 状态码非200时的返回信息
    wt.write(row_nub, 10, result['result'])  # 测试结果 pass 还是fail
    wt.write(row_nub, 11, result['msg'])
    # 抛异常
"""

# ##################################当有多个接口的结果被引用的时候#####################################
# coding:utf-8
import json
import requests
from excelddtdriver.common.writeExcel import copy_excel, Write_excel
from util.VariableDemo import read
from util.VariableDemo import reverseData
from util.customLog import getLogger
import os

session = requests.session()

# 　dictTheResultReused_t_003 = {}  # 单个接口的响应结果作为另一个接口的参数
dictTheResultReused_login_official_0014 = {}  # 两个接口的返回值作为

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 "
                  "Safari/537.36 ",
    "customSource": "10"
}

logger = getLogger(os.path.abspath(".") + "\\log\\")
readFile = os.path.abspath(".") + "\\case\\pro_data.xlsx"


# requests接口处理


def send_requests(testdata):
    dic = read(readFile, "变量")
    '''封装requests请求'''

    method = testdata["method"]
    methodType = testdata["methodType"]
    url = testdata["url"]
    IsTheResultReused = testdata["IsTheResultReused"]  # 此请求的请响应结果是否被其他接口重用
    logger.info(str(method) + ":  " + str(url))
    # url后面的params参数
    try:
        params = eval(testdata["params"])
        # 做数据替换处理
        params = reverseData(params, dic)
        logger.info("参数:  " + str(params))
    except Exception as e:
        print(e, "错误提示")
        # logger.error("错误" + str(e))
        params = None
    test_nub = testdata['ID']
    print("*******正在执行用例：-----  %s  ----**********" % test_nub)
    print("请求方式：%s, 请求url:%s" % (method, url))
    print("请求params：%s" % params)
    if IsTheResultReused == "one":
        return common_function(url, method, testdata, test_nub, methodType, params, IsTheResultReused, "userId")
    if IsTheResultReused == "two":
        return common_function(url, method, testdata, test_nub, methodType, params, IsTheResultReused, "companyId")
    if IsTheResultReused == "three":
        return common_function(url, method, testdata, test_nub, methodType, params, IsTheResultReused, "accountHolder")
    if IsTheResultReused == "accountIdCompanyId":
        return common_function(url, method, testdata, test_nub, methodType, params, IsTheResultReused, "accountIdCompanyId")
    else:
        return common_function(url, method, testdata, test_nub, methodType, params, IsTheResultReused, "zero")


# 　keyName,valueName
# **keyName 不定长参数
# 需要替换的名和值
def common_function(url, method, testdata, test_nub, methodType, params, IsTheResultReused, *keyName):
    global dictTheResultReused_login_official_0014
    if len(dictTheResultReused_login_official_0014) > 0:
        print("此时的字典数据为：  ", dictTheResultReused_login_official_0014)
        value = parse_dict(dictTheResultReused_login_official_0014, keyName)

    # print("params的类型=====>", type(params)) # 此时的参数只有一个
    #if len(keyName) == 1:
    #if keyName[0] in params.keys():
    #      params[keyName[0]] = value
    for i in range(len(keyName)):
        if keyName[i] in params.keys():
            params[keyName[i]] = value


    # 当需要替换的参数有多个的时候


    if len(IsTheResultReused) > 0:
        if method == "post" and methodType == "dict":
            r = session.post(url, data=params, headers=headers, verify=False)
            print("headers -------------->", headers)
            print("替换后的参数为", params)
            dictTheResultReused_login_official_0014[IsTheResultReused] = json.loads(r.text)

            print("headers -------------->", headers)
        elif method == "post" and methodType == "json":
            r = session.post(url, data=json.dumps(params), headers=headers, verify=False)
            print("headers -------------->", headers)
            print("替换后的参数为", params)
            dictTheResultReused_login_official_0014[IsTheResultReused] = json.loads(r.text)


        # GET 请求拼接URL
        else:
            if len(str(params)) > 0:
                url += '?' + '&'.join([str(key) + '=' + str(value) for key, value in params.items()])
                logger.info("此时的请求方式为" + method + "此时的URL为 ： " + url)
                r = session.get(url, headers=headers, verify=False)
                print("替换后的参数为", params)
                print("headers -------------->", headers)
                dictTheResultReused_login_official_0014[IsTheResultReused] = json.loads(r.text)

        # print("此时的dictTheResultReused_t_009_011字典的结果为-------->", dictTheResultReused_t_009_011)
    else:
        if method == "post" and methodType == "dict":
            r = session.post(url, data=params, headers=headers, verify=False)
            print("替换后的参数为", params)
            print("headers -------------->", headers)
        elif method == "post" and methodType == "json":
            r = session.post(url, data=json.dumps(params), headers=headers, verify=False)
            print("替换后的参数为", params)
            print("headers -------------->", headers)

        # GET 请求拼接URL
        else:
            if len(str(params)) > 0:
                url += '?' + '&'.join([str(key) + '=' + str(value) for key, value in params.items()])
                logger.info("此时的请求方式为" + method + "此时的URL为 ： " + url)
                print("替换后的参数为", params)
                r = session.get(url, headers=headers, verify=False)

    if "token" in r.text:
        token = json.loads(r.text).get("res").get("token")
        headers["Authorization"] = token

    res = {"result": ""}  # 接受返回数据
    try:
        print("页面返回信息：%s" % r.text)
        res['ID'] = testdata['ID']
        res['rowNum'] = testdata['rowNum']
        res["statusCode"] = str(r.status_code)  # 状态码转成str
        res["text"] = r.text
        res["times"] = str(r.elapsed.total_seconds())  # 接口请求时间转str

        if res["statusCode"] != "200":
            res["error"] = res["text"]
        else:
            res["error"] = ""
        res["msg"] = ""
        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
            # print("用例测试结果:   %s---->%s" % (test_nub, res["result"]))
        else:
            res["result"] = r.text
        logger.info("接口返回的结果为:  " + str(res))
        return res
    # 捕获到异常的时候会写入Msg
    except Exception as msg:
        res["msg"] = str(msg)
        logger.info("捕获异常，接口返回的结果为:" + str(res))
        return res


# 针对接口解析需要复用的字典 返回一个需要的类型
def parse_dict(dic, keyName):
    # l2_dict_003 = []
    # print("此时的字典的数据位===============>", dic)

    try:

        # l1 = dic.get("login_official_0014").get("res").get("userId")

        if keyName[0] == "companyId":
            l1 = dic.get(keyName[0]).get("res")[-1].get("id")
        elif keyName[0] == "userId":
            l1 = dic.get(keyName[0]).get("res").get(keyName[0])
        elif keyName[0] == "addClient":
            l1 = dic.get(keyName[0]).get("res").get(keyName[0])
        elif keyName[0] == "accountHolder":
            l1 = dic.get(keyName[0]).get("res").get(keyName[0]).get("id")
        elif keyName[0] == "accountIdCompanyId":
            l1 = dic.get(keyName[0]).get("res").get("records")[0].get("accountId") +"," + dic.get(keyName[1]).get("res").get("records")[0].get("companyId")
        else:
            l1 = ""
    except Exception as e:
        print(e)
        l1 = ""

    return l1


def wirte_result(result, filename="result.xlsx"):
    # 返回结果的行数row_nub
    print(result)
    row_nub = result['rowNum']
    # statusCode
    wt = Write_excel(filename)
    wt.write(row_nub, 6, result['statusCode'])  # 写入返回状态码statusCode,第8列
    wt.write(row_nub, 7, result['times'])  # 耗时
    wt.write(row_nub, 8, result['error'])  # 状态码非200时的返回信息
    wt.write(row_nub, 10, result['result'])  # 测试结果 pass 还是fail
    wt.write(row_nub, 11, result['msg'])
    # 抛异常

# _*_ coding:utf-8 _*_

# 读取Excel中的变量将数据放置到字典中
import xlrd
import random

"""
此方法是将用例中的变量放置到字典中，待执行用例之前将数据加载到缓存中,为之后的数据替换做准备
"""


# 此方法是获取变量
def read(path, sheetName):
    dic = {}
    l = []
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(sheetName)
    for i in range(1, table.nrows):
        l.append(table.row_values(i))
    for j in l:
        ls = str(j[1])
        if "." in ls:
            ls = ls[:-2]
        dic[j[0]] = ls
        #print(ls)

    return isNullAndReplace(dic)


# 替换变量
def reverseData(dic1, dic2):
    for k, v in dic1.items():
        if v in dic2.keys():
            dic1[k] = dic2.get(v)

    return dic1


# 当参数值为空的时候可以促发此方法
def makeData():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
               "153", "155", "156", "157", "158", "159", "186", "187", "188"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


# 判断字典中是否有value为空字符串的数据 并且进行替换
# {'${username}': '15271892099', '${password}': '123456', '${test}': ''}
def isNullAndReplace(dic):
    for k, v in dic.items():
        if len(v) == 0:  # 判断当字典中值为空字符串的时候，进行替换
            dic[k] = makeData()
    return dic


if __name__ == "__main__":
    print(read("D:\\file\\pWorkSpace\\excelddtdriver\\case\\invoice_data.xlsx", "变量"))
    # print(makeData())

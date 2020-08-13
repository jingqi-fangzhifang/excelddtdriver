# _*_ coding:utf-8 _*_

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure(figsize=(80,60))
df = pd.read_excel('result.xlsx')
x = df['ID']
y1 = df['times']

for a, b in zip(x, y1):
    plt.text(a, b + 0.001, "%.3f" % b, ha='center', va='bottom', fontsize=9)

x1 = []
yy = []

x2 = []
y2 = []
y = dict(zip(x, y1))

plt.bar(0, 0, label='运行时间大于1秒', color=['r'])
plt.bar(0, 0, label='运行时间小于1秒', color=['g'])
for k, v in y.items():
    if v > 1:
        x2.append(k)
        y2.append(v)
        plt.bar(x2, y2, color=['r'])
    else:
        x1.append(k)
        yy.append(v)
        plt.bar(x1, yy, color=['g'])
# x轴数据旋转90度
plt.xticks(rotation=90)

plt.xlabel('用例')
plt.ylabel('用例接口响应时间')
plt.title("xxx接口测试时间统计")
plt.legend()
plt.show()

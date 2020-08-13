# _*_ coding:utf-8 _*_

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
df = pd.read_excel('result.xlsx')
x = df['ID']
y1 = df['times']

count0 = 0
count1 = 0
count2 = 0
for i in y1:
    if i <= 0.4:
        count0 += 1
    elif 0.5 >= i > 0.4:
        count1 += 1
    else:
        count2 += 1
data = [count0, count1, count2]
labels = ["时间小于0.4s", "时间大于0.4s小于0.5s", "时间大于0.5s"]
cols = ['g', 'yellow', 'red']  # y颜色
plt.axis('equal')
plt.pie(data, labels=labels, autopct='%1.1f%%', colors=cols)
plt.title(u'接口响应时间分布图')
plt.show()

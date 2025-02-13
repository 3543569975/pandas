import pandas as pd


dict_sr = {'Name':pd.Series(['meng','cai','zhang','wang','li','qiang','yang']),
           'Age':pd.Series([20,21,22,21,22,19,20]),
           'Rating':pd.Series([2.65,3.51,2.98,3.22,2.70,3.6,4.1])}
df = pd.DataFrame(dict_sr)

#sum函数
print('初始数据：\n{}'.format(df))
print('轴的值总和：\n{}'.format(df.sum()))
#行轴的值总和
print('行轴的总和：\n{}'.format(df.sum(1)))

#mean函数：返回平均值
print('轴的平均值：\n{}'.format(df.mean()))

#std函数：返回数字列的Bressel标准偏差
print('标准偏差：\n{}'.format(df.std()))

#describe函数：计算有关DataFrame列的统计信息的摘要
print('初始数据：\n{}'.format(df))
print('汇总数据：\n{}'.format(df.describe()))
#include函数：object汇总字符串系列，number汇总数字列，all将所有列汇总
#object
print('初始数据：\n{}'.format(df))
print('include为object的标准偏差：\n{}'.format(df.describe(include=['object'])))
#all
print('初始数据：\n{}'.format(df))
print('include为all的标准偏差：\n{}'.format(df.describe(include='all')))


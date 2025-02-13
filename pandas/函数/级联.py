import pandas as pd
import numpy as np


#concat(objs,axis=0,join='outer',join_axes=None,ignore_index=False)，完成沿轴执行级联操作的所有重要工作。
#objs:Series、DataFrame、Panel对象的序列或映射。axis:默认为0，连接轴。
#join:{’inner，‘outer'},默认inner，联合外部和交叉内部来处理其他轴上的索引。
#join_axes:是index对象的列表，用于其他（n-1）轴的特定索引，而不是执行内部、外部逻辑。
#ignore_index:布尔值，默认False。如果指定为True，则不要使用连接轴上的索引值。结果轴将被标记为0，1，……，n-1.

first = pd.DataFrame({
    'Name':['meng','zhi','wang'],
    'number':['1001','1002','1003'],
    'score':[98,95,91]},
    index=[1,2,3])
second = pd.DataFrame({
    'Name':['li','zhang','ming'],
    'number':['1001','1002','1005'],
    'score':[93,100,97]},
    index=[1,2,3])
rs = pd.concat([first,second])
print('对象连接：\n{}'.format(rs))

#通过键参数把特定的键与每个碎片的DataFrame关联起来
rs = pd.concat([first,second],keys=['x','y'])
print('使用键参数关联碎片：\n{}'.format(rs))

#如果想要生成对象必须遵顼自己的索引，则将ignore_index设置为True
rs = pd.concat([first,second],keys=['x','y'],ignore_index=True)
print('使生成的对象遵循自己的索引：\n{}'.format(rs))

#如果需要沿axis = 1,则添加两个对象
rs = pd.concat([first,second],axis=1)
print('沿axis设置值添加对象：\n{}'.format(rs))

#append
rs = first.append(second)
print('append函数带一个对象：\n{}'.format(rs))
rs = first.append([second,first])
print('append函数带多个对象：\n{}'.format(rs))

#时间序列
print('当前时间：{}'.format(pd.datetime.now()))
pd_time = pd.Timestamp('2019-01-23')
print('创建一个时间戳：{}'.format(pd_time))
pd_time = pd.Timestamp(1588686880,unit='s')
print('时间戳转时间：{}'.format(pd_time))
pd_time = pd.date_range('12:00','23:59',freq='30min').time
print('创建一个时间范围：\n{}'.format(pd_time))
pd_time = pd.date_range('12:00','23:59',freq='H').time
print('改变时间的频率：\n{}'.format(pd_time))
pd_time = pd.to_datetime(pd.Series(['Jul 31 2009','2019-10-10',None]))
print('转换为时间戳：\n{}'.format(pd_time))
pd_time = pd.to_datetime(['2019/01/23','2019.12.31',None])
print('时间转换：{}'.format(pd_time))
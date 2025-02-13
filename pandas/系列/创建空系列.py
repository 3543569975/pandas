import pandas as pd


#Series(data,index,dtype,copy):
#data:数据采取各种形式（ndarry，list，constans）。index:索引值必须是唯一的和散列的，与数据的长度相同。
#dtype:指定数据类型。copy:是否复制数据，默认False。

#创建空系列
empty_s = pd.Series()
print('创建空系列：{}'.format(empty_s))

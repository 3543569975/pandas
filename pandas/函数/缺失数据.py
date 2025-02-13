import pandas as pd
import numpy as np


#检查缺失值
df = pd.DataFrame(np.random.randn(3,3),index=['a','c','e'],columns=['one','two','three'])
df = df.reindex(['a','b','c','d','e'])
print(df)
#对应元素是否为NaN。若为NaN，则结果为True；否则为False
print(df['one'].isnull())
#对应元素是否不为NaN。若不为NaN，则结果为True；否则为False
print(df['one'].notnull())

#缺失数据的计算
df = pd.DataFrame(np.random.randn(3,3),index=['a','c','e'],columns=['one','two','three'])
df = df.reindex(['a','b','c'])
print('df数组：\n{}'.format(df))
print('df数组求和：\n{}'.format(df['one'].sum()))
pd_df = pd.DataFrame(index=[0,1,2,3,4,5],columns=['one','two'])
print('pd_df数组：\n{}'.format(pd_df))
print('pd_df数组求和:\n{}'.format(pd_df['one'].sum))

#缺失数据填充
df = pd.DataFrame(np.random.randn(3,3),index=['a','c','e'],columns=['one','two','three'])
df = df.reindex(['a','b','c','d','e'])
print('df数组：\n{}'.format(df))
print('用0填充NaN后的数组：\n{}'.format(df.fillna(0)))

#向前或向后填充
df = pd.DataFrame(np.random.randn(3,3),index=['a','c','e'],columns=['one','two','three'])
df = df.reindex(['a','b','c','d','e'])
print('df数组：\n{}'.format(df))
print('向前填充NaN后的数组：\n{}'.format(df.fillna(method='pad')))
print('向后填充NaN后的数组：\n{}'.format(df.fillna(method='backfill')))

#清除缺失值
df = pd.DataFrame(np.random.randn(3,3),index=['a','c','e'],columns=['one','two','three'])
df = df.reindex(['a','b','c','d','e'])
print('df数组：\n{}'.format(df))
print(df.dropna())
print(df.dropna(axis=1))

#值替换
df = pd.DataFrame({'one':[10,20,30,40,50,2000],'two':[1000,0,30,40,50,60]})
print(df.replace({1000:10,2000:60}))
import pandas as pd
import numpy as np


#在整个DataFrame上应用聚合:可通过向整个DataFrame传递一个函数进行聚合，也可以通过标准的获取项目方法选择一个列。
df = pd.DataFrame(np.random.randn(2,4),index=pd.date_range('1/1/2019',periods=2),
                  columns=['A','B','C','D'])
print('初始数组：\n{}'.format(df))
r1_df = df.rolling(window = 3,min_periods = 1)
print('在整个DataFrame上应用聚合：\n{}'.format(r1_df.aggregate(np.sum)))

#在DataFrame的单列上应用聚合
df = pd.DataFrame(np.random.randn(2,4),index=pd.date_range('1/1/2019',periods=2),
                  columns=['A','B','C','D'])
print('初始数组：\n{}'.format(df))
r1_df = df.rolling(window = 3,min_periods = 1)
print('在DataFrame的单列上应用聚合：\n{}'.format(r1_df['A'].aggregate(np.sum)))

#在DataFrame的多列上应用聚合
df = pd.DataFrame(np.random.randn(2,4),index=pd.date_range('1/1/2019',periods=2),
                  columns=['A','B','C','D'])
print('初始数组：\n{}'.format(df))
r1_df = df.rolling(window = 3,min_periods = 1)
print('在DataFrame的多列上应用聚合：\n{}'.format(r1_df['A','B'].aggregate(np.sum)))

#在DataFrame的单列上应用多个函数
df = pd.DataFrame(np.random.randn(2,4),index=pd.date_range('1/1/2019',periods=2),
                  columns=['A','B','C','D'])
print('初始数组：\n{}'.format(df))
r1_df = df.rolling(window = 3,min_periods = 1)
print('在DataFrame的单列上应用多个函数：\n{}'.format(r1_df['A'].aggregate([np.sum,np.mean])))

#在DataFrame的多列上应用多个函数
df = pd.DataFrame(np.random.randn(2,4),index=pd.date_range('1/1/2019',periods=2),
                  columns=['A','B','C','D'])
print('初始数组：\n{}'.format(df))
r1_df = df.rolling(window = 3,min_periods = 1)
print('在DataFrame的多列上应用多个函数：\n{}'.format(r1_df['A','B'].aggregate([np.sum,np.mean])))

#将不同函数应用于DataFrame的不同列
df = pd.DataFrame(np.random.randn(2,4),index=pd.date_range('1/1/2019',periods=2),
                  columns=['A','B','C','D'])
print('初始数组：\n{}'.format(df))
r1_df = df.rolling(window = 3,min_periods = 1)
print('将不同函数应用于DataFrame的不同列：\n{}'.format(r1_df.aggregate({'A':np.sum,'B':np.mean})))

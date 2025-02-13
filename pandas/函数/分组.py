import pandas as pd
import numpy as np


#将数据拆分成组
df_data = {'Team':['A','B','C','B','A','D','C'],
           'Rank':[1,2,2,3,3,4,1],
           'Year':[2018,2019,2020,2019,2018,2020,2021],
           'Points':[87.5,81,86,79.5,76,89,75]}
df = pd.DataFrame(df_data)
print(df.groupby('Team'))

#查看分组
print(df)
print('按一列分组：\n{}'.format(df.groupby('Team').groups))
print('按多列分组：\n{}'.format(df.groupby(['Team','Year']).groups))

#迭代遍历分组
print(df)
grouped = df.groupby('Year')
for name,group in grouped:
    print(name)
    print(group)

#选择一个分组
print('选择一个分组2019')
print(grouped.get_group(2019))

#聚合
print('按Points聚合：\n{}'.format(grouped['Points'].agg(np.mean)))
grouped = df.groupby('Team')
print('按Team分组查看大小：\n{}'.format(grouped.agg(np.size)))

#使用多个聚合函数
grouped = df.groupby('Team')
agg = grouped['Points'].agg([np.sum,np.mean,np.std])
print(agg)

#转换
grouped = df.groupby('Team')
score = lambda x:(x-x.mean())/x.std()*10
print(grouped.transform(score))

#过滤
print(df)
filter = df.groupby('Team').filter(lambda x:len(x)>=2)
print(filter)
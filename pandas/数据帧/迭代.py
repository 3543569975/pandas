import pandas as pd
import numpy as np


#迭代DataFrame提供列名
N = 20
df = pd.DataFrame({
    'A':pd.date_range(start='2016-01-01',periods=N,freq='D'),
    'x':np.linspace(0,stop=N-1,num=N),
    'y':np.random.rand(N),
    'C':np.random.choice(['Low','Medium','High'],N).tolist(),
    'D':np.random.normal(100,10,size=N).tolist()
    })
print('列名')
for col in df:
    print(col)

#遍历DataFrame函数中的行
#iteritems:迭代（key,value）对
#iterrows:将行迭代为（索引，系列）对
#itertuples:以namedtuples的形式迭代行
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
print('初始数组：')
print(df)
print('iteritems键值对')
for key,value in df.iteritems():
    print(key,value)
print('iterrows行')
for row in df.iterrows():
    print(row)
#itertuples:每一行返回一个产生一个命名元组的迭代器。元组的第一个元素是行的相应索引值，而剩余的值为行值。
print('itertuples')
for row in df.itertuples():
    print(row)
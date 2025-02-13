import pandas as pd
import numpy as np


#.loc:完成基于标签的索引。切片时，也包括起始边界。整数是有效的标签，但它们是指标签而不是位置。
#.loc具有多种访问方式，单个标量标签、标签列表、切片对象、一个布尔数组。
#loc（）需要两个单列表/范围运算符，','分隔，第一个表示行，第二个表示列。
df = pd.DataFrame(np.random.randn(8,4),
                  index=['a','b','c','d','e','f','g','h'],
                  columns=['A','B','C','D'])
print(df)
print(df.loc[:,'B'])
print(df.loc[:,['A','C']])
print(df.loc[['a','b','f','h'],['A','C']])
print(df.loc['a':'c'])
print(df.loc['a']>0)

#.iloc获得纯整数索引
df = pd.DataFrame(np.random.randn(8,4),
                  columns=['A','B','C','D'])
print('iloc:')
print(df)
print(df.iloc[:4])
print(df.iloc[1:5,2:4])
print(df.iloc[[1,3,5],[1,3]])
print(df.iloc[1:3,:])
print(df.iloc[:,1:3])

#ix进行对象选择和对象子集化的混合方法。
df = pd.DataFrame(np.random.randn(8,4),
                  columns=['A','B','C','D'])
print('ix:')
print(df.ix[:4])
print(df.ix[:,'A'])

#使用符号
df = pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])
print('使用符号：')
print(df['A'])
print(df[['A','B']])
print(df[2:2])

#属性访问'.'选择列
print('属性访问：')
df = pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])
print(df.A)
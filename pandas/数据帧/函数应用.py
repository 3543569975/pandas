import pandas as pd
import numpy as np

def add_num(x,y):
    return x+y

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])

#表格函数
print('初始数组：\n{}'.format(df))
print('调用函数后的数组：\n{}'.format(df.pipe(add_num,2)))

#行列合理函数
print('初始数组：\n{}'.format(df))
df.apply(np.mean)
print('调用apply函数后的数组：\n{}'.format(df))
#传递axis参数在行是上操作
df.apply(np.mean,axis=1)
print('调用apply函数传递axis=1后的数组：\n{}'.format(df))
#lambda参数
df.apply(lambda x: x.max() - x.min())
print('调用apply函数传递lambda后的数组：\n{}'.format(df))

#元素合理函数
df['col1'].map(lambda x:x*100)#df.applymap(lambda x:x*100)
print(df)
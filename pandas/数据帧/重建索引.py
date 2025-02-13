import pandas as pd
import numpy as np


#重建对象对齐索引
df_1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df_2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
print('初始数组：\n{}'.format(df_1))
df_1 = df_1.reindex_like(df_2)
print('重建对象对齐索引后的数组：\n{}'.format(df_1))

#填充时重新加注
#reindex():pad/ffill:向前填充。bfill/backfill:向后填充。nearest:从最近的索引值填充。
df_1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df_2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
print('NaN值填充：\n{}'.format(df_2.reindex_like(df_1)))
print('用前面的值填充NaN:\n{}'.format(df_2.reindex_like(df_1,method='ffill')))

#重建索引时的填充限制
df_1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df_2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
print('NaN值填充：\n{}'.format(df_2.reindex_like(df_1)))
print('正向填充限制为1的数据帧：\n{}'.format(df_2.reindex_like(df_1,method='ffill',limit=1)))

#重命名
#rename允许基于一些映射或任意函数重新标记一个轴
df_1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print('NaN值填充：\n{}'.format(df_2.reindex_like(df_1)))
print('重命名行和列后：\n{}'.format(df_1.rename(columns={'col1':'c1','col2':'c2'},
                                               index={0:'apple',1:'banana',2:'durian'})))

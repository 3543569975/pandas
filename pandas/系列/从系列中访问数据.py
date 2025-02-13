import pandas as pd

pd_sr = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print('获取第一个元素：{}'.format(pd_sr[0]))

print('获取系列前三个元素：\n{}'.format(pd_sr[:3]))
#不包含停止索引下标

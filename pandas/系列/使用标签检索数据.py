import pandas as pd

pd_sr = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print('检索单个元素：{}'.format(pd_sr['b']))
#检索多个
print('检索单个元素：{}'.format(pd_sr[['a','b','c']]))
#不包含标签出现异常
#print('检索不存在元素：{}'.format(pd_sr['w']))
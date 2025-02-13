import pandas as pd
import numpy as np


#pct_change:将每个元素与其前一个元素进行比较((3-2)/2)
pd_sr = pd.Series([1,2,3,4,5,4])
pct_ch = pd_sr.pct_change()
print('系列：\n{}'.format(pd_sr))
print('系列前后元素变化百分比：\n{}'.format(pct_ch))
df = pd.DataFrame(np.random.randn(5,2))
print('数据帧前后元素变化百分比：\n{}'.format(df.pct_change()))

#协方差
#Series.cov:计算序列之间的协方差（不包括缺失值），NaN将自动排除
#DataFrame.cov:计算DataFrame中序列之间的成对协方差，也排除NaN/null值
#DataFrame.cov:支持可选min_periods（指定每个列对所需的最小观察数，以获得有效结果）
sr_1 = pd.Series(np.random.randn(20))
sr_2 = pd.Series(np.random.randn(30))
print('Series.cov()可用于计算序列之间的协方差：\n{}'.format(sr_1.cov(sr_2)))
df = pd.DataFrame(np.random.randn(100,5),columns=['a','b','c','d','e'])
print('DataFrame.cov计算DataFrame中的序列之间的协方差：\n{}'.format(df.cov()))
df = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
df.loc[df.index[:5],'a'] = np.nan
df.loc[df.index[5:10],'b'] = np.nan
print('DataFrame.cov支持可选min_periods:\n{}'.format(df.cov(min_periods=2)))

#相关性
#pearson:标准相关系数
#kendall:Kendall Tau相关系数
#spearman:斯皮尔曼等级相关系数
df = pd.DataFrame(np.random.randn(10,4),columns=['a','b','c','d'])
print(df['a'].corr(df['b']))
print(df.corr())
df.loc[df.index[:4],'a'] = np.nan
df.loc[df.index[4:10],'b'] = np.nan
print(df.corr(min_periods=2))

#数据排名
sr_pd = pd.Series(np.random.randn(4),index=list('abcd'))
sr_pd['d'] = sr_pd['b']
print(sr_pd)
print(sr_pd.rank())

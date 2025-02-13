import pandas as pd

data_dict = {'a':0,'b':1,'c':2}
s_pd = pd.Series(data_dict)
print('由字典创建系列：\n{}'.format(s_pd))

data_dict = {'a':0,'b':1,'c':2}
s_pd = pd.Series(data_dict,index=['b','c','d','a'])
print('由字典创建系列，并自定义索引：\n{}'.format(s_pd))
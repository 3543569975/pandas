import pandas as pd
import numpy as np


#创建分类对象
sr = pd.Series(['a','b','c','a'],dtype='category')
print(sr)

#创建类别对象
cat = pd.Categorical(['a','b','c','a','b','c'])
print('示例1：\n{}'.format(cat))
cat = pd.Categorical(['a','b','c','a','b','c','d'],['c','b','a'])
print('示例2：\n{}'.format(cat))
cat = pd.Categorical(['a','b','c','a','b','c','d'],['c','b','a'],ordered=True)
print('示例3：\n{}'.format(cat))

#describe
cat = pd.Categorical(['a','c','c',np.nan],categories=['b','a','c'])
df = pd.DataFrame({'cat':cat,'s':['a','c','c',np.nan]})
print(df.describe())
print('='*40)
print(df['cat'].describe())

#获取类别和顺序
s = pd.Categorical(['a','c','c',np.nan],categories=['b','a','c'])
print('对象类别：{}'.format(s.categories))
cat = pd.Categorical(['a','c','c',np.nan],['b','a','c'])
print('对象顺序：{}'.format(cat.ordered))

#将新值分配给series.cat.categories属性实现类别重命名
sr = pd.Series(['a','b','c','a'],dtype='category')
sr.cat.categories = ['Group %s' % g for g in sr.cat.categories]
print(sr.cat.categories)

#追加新类别后的对象,删除指定类别后的对象
sr = pd.Series(['a','b','c','a'],dtype='category')
print('初始对象：\n{}'.format(sr))
sr = sr.cat.add_categories([4])
print('追加新类别后的对象：\n{}'.format(sr.cat.categories))
print('删除指定类别后的对象：\n{}'.format(sr.cat.remove_categories('a')))
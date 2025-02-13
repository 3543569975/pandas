import pandas as pd
import numpy as np


#merge(left,right,how='inner',on=None,left_on=None,right_on=None,left_index=False,right_index=False,sort=True)
#left:一个DataFrame对象。right:另一个DataFrame对象。how:是left,right,outer及inner中的一个，默认inner。
#on:列（名称）连接，必须在左侧DataFrame和右侧DataFrame对象中存在。
#left_on:来自左侧DataFrame中的列作为键，可以是列名或长度等于DataFrame长度的数组。
#right_on:来自右侧DataFrame中的列作为键，可以是列名或长度等于DataFrame长度的数组。
#left_index:如果为True,则使用左侧DataFrame中的索引（行标签）作为其连接键。
# 在具有MultiIndex(分层)的DataFrame的情况下，级别的数量必须于来自右侧DataFrame中的连接键的数量相匹配。
#right_index:同上。
#sort:按照字典顺序通过连接键对结果DataFrame进行排序。默认为True;设置为False时，在很多情况下可以大大提高性能。


#合并一个键的两个数据帧
left = pd.DataFrame({'id':[1,2,3],
                     'Name':['meng','zhi','wang'],
                     'number':['1001','1002','1003']})
right = pd.DataFrame({'id':[1,2,3],
                      'Name':['li','zhang','ming'],
                      'number':['1002','1003','1005']})
print('左数据帧：\n{}'.format(left))
print('右数据帧：\n{}'.format(right))
rs = pd.merge(left,right,on = 'id')
print('由id合并数据帧：\n{}'.format(rs))

#合并多个键上的两个数据帧
left = pd.DataFrame({'id':[1,2,3],
                     'Name':['meng','zhi','wang'],
                     'number':['1001','1002','1003']})
right = pd.DataFrame({'id':[1,2,3],
                      'Name':['li','zhang','ming'],
                      'number':['1001','1002','1005']})
rs = pd.merge(left,right,on = ['id','number'])
print('由多个键合并数据帧：\n{}'.format(rs))

#使用how参数
#left:使用左侧对象的键。right:使用右侧对象的键。outer：使用键的联合。inner：使用键的交集。
rs_left = pd.merge(left,right,on = 'number',how = 'outer')
print('left join的结果：\n{}'.format(rs_left))
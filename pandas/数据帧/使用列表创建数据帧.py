import pandas as pd


#单个列表创建数据帧
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

#嵌套列表创建数据帧
data = [['xiao meng',20],['xiao zhi',21],['xiao qiang',23]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)

#ndarrays/lists的字典创建数据帧
data = {'Name':['xiao meng','xiao zhi','xiao qiang','xiao wang'],'Age':[20,21,23,22]}
df = pd.DataFrame(data)
print(df)
#使用数组创建自定义索引的数据帧
data = {'Name':['xiao meng','xiao zhi','xiao qiang','xiao wang'],'Age':[20,21,23,22]}
df = pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])
print(df)

#字典列表创建数据帧
data = [{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df = pd.DataFrame(data,index=['first','second'])
print(df)
#字典、行索引、列索引列表创建数据帧
data = [{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df_1 = pd.DataFrame(data,index=['first','second'],columns=['a','b'])
print(df_1)
df_2 = pd.DataFrame(data,index=['fitst','second'],columns=['a','b1'])
print(df_2)

#系列的字典创建数据帧
dict_v = {'one':pd.Series([1,2,3],index=['a','b','c']),
          'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(dict_v)
print(df)

#列选择
dict_v = {'one':pd.Series([1,2,3],index=['a','b','c']),
          'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(dict_v)
print('列选择one：')
print(df['one'])

#列添加
dict_v = {'one':pd.Series([1,2,3],index=['a','b','c']),
          'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(dict_v)
df['three'] = pd.Series([10,20,30],index=['a','b','c'])
print('根据传递的系列添加新列：\n{}'.format(df))
df['four'] = df['one'] + df['three']
print('使用存在的数据帧添加新列：\n{}'.format(df))

#列删除
dict_v = {'one':pd.Series([1,2,3],index=['a','b','c']),
          'two':pd.Series([1,2,3,4],index=['a','b','c','d']),
          'three':pd.Series([10,20,30],index=['a','b','c'])}
df = pd.DataFrame(dict_v)
print('初始数据帧：\n{}'.format(df))

del df['one']
print('使用删除函数删除第一列：\n{}'.format(df))
df.pop('two')
print('使用pop函数删除一列：\n{}'.format(df))

#行选择、添加、删除

dict_v = {'one':pd.Series([1,2,3],index=['a','b','c']),
          'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(dict_v)
print(df.loc['b'])
print(df.iloc[2])

#行切片
dict_v = {'one':pd.Series([1,2,3],index=['a','b','c']),
          'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(df)
print(df[2:4])
df = pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
print('初始数据帧：\n{}'.format(df))
df2 = pd.DataFrame([[5,6],[7,8]],columns=['a','b'])
df = df.append(df2)
print('添加新行后的数据帧：\n{}'.format(df))
df = df.drop(0)
print('删除包含标签0后的数据帧：\n{}'.format(df))
import pandas as pd


#创建一个字典系列
dict_sr = {'Name':pd.Series(['meng','cai','zhang','wang','li','qiang','yang']),
           'Age':pd.Series([20,21,22,21,22,19,20]),
           'Rating':pd.Series([2.65,3.51,2.98,3.22,2.70,3.6,4.1])}
df = pd.DataFrame(dict_sr)
print('初始数据：\n{}'.format(df))


#T转置
print('初始数据：\n{}'.format(df))
print('数据帧的转置：\n{}'.format(df.T))

#axes:返回行轴标签和列轴标签列表
print('初始数据：\n{}'.format(df))
print('行轴标签和列轴标签：\n{}'.format(df.axes))

#dtype:返回每列的数据类型
print('初始数据：\n{}'.format(df))
print('各个列的数据类型：\n{}'.format(df.dtypes))

#empty:返回布尔值，空为True
print('对象是否为空：{}'.format(df.empty))

#ndim:表示轴/数组的维度大小
print('初始数据：\n{}'.format(df))
print('对象的维度为：\n{}'.format(df.ndim))

#shape:返回表示DataFrame的维度的元组
print('对象的维度元组：\n{}'.format(df.shape))

#size:返回DateFrame中的元素数
print('初始数据：\n{}'.format(df))
print('对象中的元素数：\n{}'.format(df.size))

#values:将DataFrame中的实际数据作为ndarray返回
print('初始数据：\n{}'.format(df))
print('数据框架中的实际数据：\n{}'.format(df.values))

#head:返回前n行，默认为5。
#tail:返回后n行，默认为5。
print('初始数据：\n{}'.format(df))
print('数据帧的前两行：\n{}'.format(df.head(2)))
print('数据帧的后两行：\n{}'.format(df.tail(2)))
import pandas as pd
import numpy as np


#lower:将用于Series/Index中的字符转换小写
str_list = ['meng','Zhi','MI','w@y',np.nan,'123','LiXiao']
pd_str = pd.Series(str_list)
print('lower:\n{}'.format(pd_str.str.lower()))

#upper:将用于Series/Index中的字符转换大写
str_list = ['meng','Zhi','MI','w@y',np.nan,'123','LiXiao']
pd_str = pd.Series(str_list)
print('upper:\n{}'.format(pd_str.str.upper()))

#len:计算字符串的长度
str_list = ['meng','Zhi','MI','w@y',np.nan,'123','LiXiao']
pd_str = pd.Series(str_list)
print('len:\n{}'.format(pd_str.str.len()))

#strip:删除Series/Index两侧的每个字符串中的空格（包括换行符）
str_list = [' meng','Zhi ','MI','Li Xiao']
pd_str = pd.Series(str_list)
print('strip:\n{}'.format(pd_str.str.strip('Z')))

#split:用给定模式拆分每个字符串
str_list = [' meng','Zhi ','MI','Li Xiao']
pd_str = pd.Series(str_list)
print('split:\n{}'.format(pd_str.str.split('i')))

#cat:使用给定的分隔符连接Series/Index元素
str_list = [' meng','Zhi ','MI','Li Xiao']
pd_str = pd.Series(str_list)
print('cat:\n{}'.format(pd_str.str.cat(sep='<=>')))

#get_dummies:返回具有单热编码值的数据帧
str_list = [' meng','Zhi ','MI','Li Xiao']
pd_str = pd.Series(str_list)
print('get_dummies:\n{}'.format(pd_str.str.get_dummies()))

#contains:元素中若包括子字符串，则返回每个元素的布尔值True，否则返回False
str_list = [' meng','Zhi ','MI','Li Xiao']
pd_str = pd.Series(str_list)
print('strip:\n{}'.format(pd_str.str.contains(' ')))

#replace:用于将值a替换为值b
str_list = [' meng','Zhi ','MI','Li Xiao']
pd_str = pd.Series(str_list)
print('replace:\n{}'.format(pd_str.str.replace('i','o')))

#repeat:用于重复每个元素指定的次数
str_list = [' meng','Zhi ','MI','Li Xiao']
pd_str = pd.Series(str_list)
print('repeat:\n{}'.format(pd_str.str.repeat(2)))

#count:返回模式中每个元素出现的次数
str_list = [' meng','Zhi ','MI','Li Xiao']
pd_str = pd.Series(str_list)
print('count:\n{}'.format(pd_str.str.count('i')))

#startswith:函数的Series/Index中的元素若以模式开始，则返回True
str_list = [' meng','Zhi ','MI','Li Xiao']
pd_str = pd.Series(str_list)
print('startswith:\n{}'.format(pd_str.str.startswith('M')))

#endswith：函数的Series/Index中的元素若以模式结束，则返回True
str_list = [' meng','Zhi ','MI','Li Xiao']
pd_str = pd.Series(str_list)
print('endswith:\n{}'.format(pd_str.str.endswith('o')))

#find：返回模式第一次出现的位置
str_list = [' meng','Zhi ','MI',' Li Xiao']
pd_str = pd.Series(str_list)
print('find:\n{}'.format(pd_str.str.find('i')))

#findall:返回模式出现的所有列表
str_list = [' meng','Zhi ','MI',' Li Xiao']
pd_str = pd.Series(str_list)
print('findall:\n{}'.format(pd_str.str.findall('i')))

#swapcase:用于变换字母大小写
str_list = [' meng','Zhi ','MI',' Li Xiao']
pd_str = pd.Series(str_list)
print('swapacase:\n{}'.format(pd_str.str.swapcase()))

#isupper:用于检查Series/Index中每个字符串的所有字符是否是大写形式，返回布尔值
str_list = [' meng','Zhi ','MI',' Li Xiao']
pd_str = pd.Series(str_list)
print('isupper:\n{}'.format(pd_str.str.isupper()))

#isnumeric:用于检查Series/Index中每个字符串的所有字符是否为数字，返回布尔值
str_list = [123,'123','MI',' Li Xiao']
pd_str = pd.Series(str_list)
print('isnumeric:\n{}'.format(pd_str.str.isnumeric()))
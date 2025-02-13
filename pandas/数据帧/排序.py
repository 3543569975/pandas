import pandas as pd
import numpy as np


#按标签排序
un_sorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print('排序前：\n{}'.format(un_sorted_df))
sorted_df = un_sorted_df.sort_index()
print('排序后：\n{}'.format(sorted_df))

#排序顺序(将布尔值传递给升序参数，可以控制排序顺序)。
un_sorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print('排序前：\n{}'.format(un_sorted_df))
sorted_df = un_sorted_df.sort_index(ascending=False)
print('排序后：\n{}'.format(sorted_df))

#按列排序（0行(默认情况，对行标签排序),1列(对列标签排序)）
un_sorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print('排序前：\n{}'.format(un_sorted_df))
sorted_df = un_sorted_df.sort_index(axis = 0)
print('排序后：\n{}'.format(sorted_df))

#按值排序（升序）
un_sorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
print('排序前：\n{}'.format(un_sorted_df))
sorted_df = un_sorted_df.sort_values(by='col1')
print('排序后：\n{}'.format(sorted_df))

#排序算法
#快排quicksort、归并mergesort、堆排序heapsort、稳定排序stable，默认快排
un_sorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
print('排序前：\n{}'.format(un_sorted_df))
sorted_df = un_sorted_df.sort_values(by='col1',kind = 'mergesort')
print('排序后：\n{}'.format(sorted_df))
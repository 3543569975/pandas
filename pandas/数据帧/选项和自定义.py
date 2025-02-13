import pandas as pd

#display常用参数
#max_rows:要显示的最大行数。max_columns:最大列数。expand_frame_repr:显示数据帧以拉伸页面。
#max_colwidth:最大列宽。precision:显示十进制的精度。

#get_option:需要一个参数，并返回指定输出中的值
print('get_option:')
print('display.max_rows = {}'.format(pd.get_option('display.max_rows')))
print('display.max_columns = {}'.format(pd.get_option('display.max_columns')))

#set_option:需要两个参数，并将该值设置为指定的参数值
print('set_option:')
print('before set display.max_rows = {}'.format(pd.get_option('display.max_rows')))
pd.set_option('display.max_rows',500)
print('after set display.max_rows = {}'.format(pd.get_option('display.max_rows')))
print('before set display.max_columns = {}'.format(pd.get_option('display.max_columns')))
pd.set_option('display.max_columns',50)
print('after set display.max_columns = {}'.format(pd.get_option('display.max_columns')))

#reset_option:接受一个参数，并将其设置为默认值
#使用reset_option函数可以将display.max_rows更改回显示的默认行数
pd.set_option('display.max_rows',500)
print('after set display.max_rows = {}'.format(pd.get_option('display.max_rows')))
pd.reset_option('display.max.rows')
print('reset display.max_rows = {}'.format(pd.get_option('display.max_rows')))

#describe_option:用于打印参数的描述
print('describe_option:')
pd.describe_option('display.max_rows')

#option_context:上下文管理器，用于临时设置语句的选项。当退出使用块时，选项值将自动恢复。
#使用option_context可以临时设置display.max_rows值
with pd.option_context('display.max_rows',50):
    print(pd.get_option('display.max_rows'))
    print(pd.get_option('display.max_rows'))
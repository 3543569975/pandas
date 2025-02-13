import pandas as pd
import numpy as np

#Panel(data,items,major_axis,minor_axis,dtype,copy)
#data:数据采取各种形式。items：axis=0。
#major_axis:axis=1。minor_axis:axis=2。
#dtype:每列数据类型。copy:复制数据。

#3Dndarry创建面板的示例：
data = np.random.rand(2, 4, 5)
data1 = {'Name':['xiao meng','xiao zhi','xiao qiang','xiao wang'],'Age':[20,21,23,22]}
ppp = pd.Panel(data1)
print(ppp)

#DataFrame对象的dict创建面板的示例：
data = {'item_1':pd.DataFrame(np.random.randn(4,3)),
        'item_2':pd.DataFrame(np.random.randn(4,2))}
p = pd.Panel(data)
print(p)

#创建空面板
p = pd.Panel()
print(p)

#使用items从面板中选择数据：
data = {'item_1':pd.DataFrame(np.random.randn(4,3)),
        'item_2':pd.DataFrame(np.random.randn(4,2))}
p = pd.Panel(data)
print(p['item_1'])

#panel.major_axis(index)方法访问数据的示例：
data = {'item_1':pd.DataFrame(np.random.randn(4,3)),
        'item_2':pd.DataFrame(np.random.randn(4,2))}
p = pd.Panel(data)
print(p.major_xs(1))

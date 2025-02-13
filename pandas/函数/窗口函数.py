import pandas as pd
import numpy as np

#rolling:应用于一系列数据。指定window=n,并在数据上应用适当的统计函数。
df = pd.DataFrame(np.random.randn(6,4),index=pd.date_range('1/1/2019',periods=6),
                  columns=['A','B','C','D'])
print(df.rolling(window=3).mean())

#expanding:应用于一系列数据。指定min_periods=n,并在数据上应用适当的统计函数。
df = pd.DataFrame(np.random.randn(6,4),index=pd.date_range('1/1/2019',periods=6),
                  columns=['A','B','C','D'])
print(df.expanding(min_periods=3).mean())

#ewm:应用于一系列数据。指定参数com、span、halflife,并在数据上应用适当的统计函数。
df = pd.DataFrame(np.random.randn(6,4),index=pd.date_range('1/1/2019',periods=6),
                  columns=['A','B','C','D'])
print(df.ewm(com=0.5).mean())

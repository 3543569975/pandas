import pandas as pd
import numpy as np


ts = pd.Series(np.random.randn(5))
ts[2:-1] = np.nan
sts = ts.to_sparse()
print(sts)

#to_dense:将任何稀疏对象转换为标准密集形式
ts = pd.Series(np.random.randn(10))
ts[2:-2] = np.nan
sts = ts.to_dense()
print(sts.to_dense())

import pandas as pd
import numpy as np

#date_range默认频率是日历中的自然日，bdate_range默认频率是工作日。
#时间序列偏移别名：B工作频率，BQS商务季度开始频率，D自然日频率，A年度结束频率，
# W每周频率，BA商务年度结束，M月结束频率，BAS商务年度开始频率，SM半月结束频率，BH商务时间频率，BM商务月结束频率，H小时频率，
# MS月起始频率，T,min分频率，SMS,SMS半开始频率，S秒频率，BMS商务月开始频率，
# L,ms毫秒，Q季度结束频率，U,us微秒，BQ商务季度结束频率，N纳秒，QS季度开始频率


#date_range:创建日期序列，默认频率为天。freq:默认为天，若设置freq参数，默认为每月最后一天。
date_list = pd.date_range('2019/01/23',periods=5)
print(date_list)
#更改日期频率
date_list = pd.date_range('2019/01/23',periods=5,freq='M')
print('最大日期频率：\n{}'.format(date_list))

#bdate_range:表示商业日期范围，不包括星期六、星期日。
date_list = pd.bdate_range('2019/01/23',periods=5)
print('指定开始日期的商业日期：\n{}'.format(date_list))
#指定起始日期
start = pd.datetime(2019,1,23)
end = pd.datetime(2019,1,28)
b_dates = pd.bdate_range(start,end)
print('指定起始日期的商业日期：\n{}'.format(b_dates))
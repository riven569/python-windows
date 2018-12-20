# 从csv文件导入数据的方法

import pandas as pd
import numpy as np

# pd.read_csv test
df_csvload= pd.read_csv(r'C:\Users\LJ\Desktop\table 2018.12.20.csv',header=0,names=range(3),index_col=0,encoding='gb2312')

print(df_csvload)

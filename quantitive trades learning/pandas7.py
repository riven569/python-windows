# 从api文件导入数据

import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime

df_csvsave=web.DataReader('600708.SS','yahoo',datetime.datetime(2018,1,1),datetime.date.today())

print(df_csvsave)
print(df_csvsave.index)
print(df_csvsave.columns)

df_csvsave.to_csv(r'C:\Users\LJ\Desktop\table.csv',columns=df_csvsave.columns,index=True)

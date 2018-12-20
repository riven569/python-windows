import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime

#获取csv数据
df_csvload=pd.read_csv(r'C:\Users\LJ\Desktop\table.csv',parse_dates=True,index_col=0,encoding='gb2312')
''''
print(df_csvload.head(3))
print(df_csvload.tail(3))
print(df_csvload.columns)
print(df_csvload.index)

print(df_csvload.shape)
print(df_csvload.describe())

print(df_csvload.info())
'''
df_csvload=df_csvload.fillna(method='ffill',axis=0,inplace=True)
print(df_csvload)
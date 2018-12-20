#股票数据特殊值处理的方法
#round()、astype applymap lamdba
import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime

df_csvload=pd.read_csv(r'C:\Users\LJ\Desktop\table.csv',parse_dates=True,index_col=0,encoding='gb2312')

#'%0.2f'%x
#df_csvload=df_csvload.applymap(lambda x:'%0.2f'%x)
#df_csvload.Volume=df_csvload.loc[:,['Volume']].apply(lambda x:'%0.0f'%x,axis=1)

#推荐该方法来修改数值精度
df_csvload=df_csvload.round(2)
df_csvload.Volume=df_csvload.Volume.astype(int)
#print(df_csvload.describe())

#print(df_csvload.head(5))


df_csvload.loc[df_csvload.loc[:,'High']==3.16,'High']=df_csvload.High.median()
print(df_csvload[df_csvload.values==3.16])


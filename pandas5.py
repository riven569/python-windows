import pandas as pd
import numpy as np

#series 组成的字典形式创建
data={'one':pd.Series([1.,2.,3.],index=['a','b','c']),
      'two':pd.Series([1.,2,3,4.],index=['a','b','c','d'])}
df=pd.DataFrame(data,index=['a','b','c','d'],columns=['one','two'])

print(df)
''''
print(df.index)
print(df.columns)
print(df.values)

print(df['one'])
print(df.one)
print(df[0:3])
print(df.loc[:,['one','two']])
print(df.iloc[[0,2],[0,1]])
'''
print(df.ix[[0,1],[0,1]])
print(df.ix[df.one>1,:1])


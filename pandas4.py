# dataframe数据对象的生成，用的情况更多一些

import pandas as pd
import numpy as np
"""
#series 组成的字典形式创建
data={'one':pd.Series([1.,2.,3.],index=['a','b','c']),
      'two':pd.Series([1.,2,3,4.],index=['a','b','c','d'])}

df=pd.DataFrame(data,index=['d','b','a'],columns=['two','three'])
print(df)

"""
"""
#字典的列表形式创建
data=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df=pd.DataFrame(data,index=['first','second'],columns=['a','b'])

print (df)
"""

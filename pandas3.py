# dataframe数据对象的生成，用的情况更多一些

import pandas as pd
import numpy as np

#列表组成的字典形式
df=pd.DataFrame({'one':[1,2,3,5],'two':[1,2,3,4]})
# print(df)

#以嵌套列表形式构建
df=pd.DataFrame([[1,2,3,5],[1,2,3,4]],index=['a','b'],columns=['one','two','three','four'])


print(df)
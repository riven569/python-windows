# dataframe数据对象的生成，用的情况更多一些

import pandas as pd
import numpy as np

#列表组成的字典形式
#df=pd.DataFrame({'one':[1,2,3,5],'two':[1,2,3,4]})
# print(df)

#以嵌套列表形式构建
#df=pd.DataFrame([[1,2,3,5],[1,2,3,4]],index=['a','b'],columns=['one','two','three','four'])

# 二维ndarray 创建
data=np.zeros((2),dtype=[('A','i4'),('B','f4'),('C','a')])
data[:]=[(1,2.,'hello'),(2,4.,'world')]
df=pd.DataFrame(data,index=['first','second'],columns=['C','A','B'])


print(df)
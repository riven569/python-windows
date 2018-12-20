# series 数据对象的访问
#以字典作为数据类型创建series对象

import pandas
import numpy as np
s=pandas.Series({'a':0,'b':1,'c':2},index=["a","b","c","d","e","f"])

print(s[:2])
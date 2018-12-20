import pandas
import numpy as np

#s=pandas.Series([-1.2,-1.3,-1.5,-1.6,-1.7,-1.8],index=["a","b","c","d","e","f"])
s=pandas.Series(["a",-1.3,-1.5,-1.6,-1.7,-1.8],index=["a","b","c","d","e","f"])

# dtype 指定为int8
s=pandas.Series([-1.2,-1.3,-1.5,-1.6,-1.7,-1.8],index=["a","b","c","d","e","f"],dtype='int8')

#ndarry 数据类型创建series对象
s=pandas.Series(np.random.randn(6),index=["a","b","c","d","e","f"])

#没有索引的情况
s=pandas.Series(np.random.randn(6))

#以字典作为数据类型创建series对象
s=pandas.Series({'a':0,'b':1,'c':2},index=["a","b","c","d","e","f"])

#以常量值为数值类型创建series对象

s=pandas.Series(5.,index=["a","b","c","d","e","f"])
print(s)
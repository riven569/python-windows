#-*-coding:utf-8-*-
h=0
cc=1
from math import sqrt
for m in range (101,201):
    for i in range(2,m-1):
        if m % i == 0:
            cc = 0
            break
    if cc==1:
        print(m)
        h+=1
    cc=1
print('the total is %d'%h)

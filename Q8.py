#-*-coding:utf-8-*-
for i in range (1,10):
    for j in range (1,10):
        result=i*j
        if i <= j:
            print('%d * %d = %d' %(i,j,result))
        
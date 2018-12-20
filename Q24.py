#-*-coding:utf-8-*-
l=[]
a=2
b=1
sum=0
for i in range(0,20):
    k=a/b
    a=a+b
    b=a-b
    sum+=k
    print (k)
    print(sum)
    
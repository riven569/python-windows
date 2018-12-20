#-*-coding:utf-8-*-
def fact(i):
    sum=0
    if i==0:
        sum =1
    else:
        sum=fact(i-1)*i
    return sum
print (fact(5))
        
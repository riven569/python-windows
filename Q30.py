#-*-coding:utf-8-*-
x=int(input('input a number (5):'))
a =x//10000
b =x%10000//1000
c =x%1000//100
d =x%100//10
e =x%10
if a==e and b==d:
    print ('it is a 回文数')
else:
    print("it is false")
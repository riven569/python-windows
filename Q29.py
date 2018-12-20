#-*-coding:utf-8-*-
x=int(input('input integer:\n'))
a =x//10000
b =x%10000//1000
c =x%1000//100
d =x%100//10
e =x%10
if a!=0:
    print ('5',e,d,c,b,a)
elif b!=0:
    print('4',d,c,b,a)
elif c!=0:
    print('3',c,b,a)

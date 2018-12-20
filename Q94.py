#-*-coding:utf-8-*-
import random
a=random.randint(1,100)
b=int(input('please guess:'))
while a!=b:
    if a>b:
        print("too small")
        b = int(input('please guess:'))
    elif a<b:
        print('too big')
        b = int(input('please guess:'))
else:
    print ('congratulate，you are great!!!')




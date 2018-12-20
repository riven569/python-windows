#-*-coding:utf-8-*-
s=100
h=s/2
i=0
for i in range(2,11):
    s+=2*h
    h/=2
print(s,h)

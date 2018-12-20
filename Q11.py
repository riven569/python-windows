#-*-coding:utf-8-*-
l=[]
a=1
b=1
for i in range (1,21):
    "print(a,b)"
    a=a+b
    b=b+a
    l.append(a)
    l.append(b)
    l.sort()
print(l)



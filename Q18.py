#-*-coding:utf-8-*-
t=0
l=[]
sum=0
a=int(input('a=:\n'))
n=int(input('n=:\n'))
for i in range (n):
    t=t+a
    a=a*10
    l.append(t)
    print (t)
print (l)
for item in l:
    sum=sum+item
print (sum)
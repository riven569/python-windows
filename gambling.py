"A B打赌,A为庄"
import random
A=8000
B=500
s=0
k=0

while A>0 and B>0:
    a = random.randint(0,1)
    b = random.randint(0,1)
    if a>b:
        A-=8
        B+=8
    if a<b:
        A-=2
        B+=2
    if a==b:
        A+=5
        B-=5
        k += 1
    s+=1
    print(a, b, A, B)
print(a,b,A,B,s,k)


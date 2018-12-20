#-*-coding:utf-8-*-
sum=0
k=1
for i in range (1,101):
        for n in range (2,i):
            if i>1:
                if (i%n) == 0:
                    k=0
                    break
        if k==1:
            print(i)
            sum+=1
        k=1
print(sum)








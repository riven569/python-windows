#-*-coding:utf-8-*-
from sys import stdout
filename=input('enter the title:\n')
fp=open(filename,'w')
ch=input('enter the string:\n')
while ch!='#':
    fp.write(ch)
    stdout.write(ch)
    ch=input('\n')
fp.close()





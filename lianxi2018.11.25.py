import bs4,requests,re
from bs4 import BeautifulSoup

from urllib.request import urlopen

#
# url='http://www.pythonchallenge.com/pc/def/equality.html'
# html=urlopen(url).read().decode()
#
#
# text=re.findall('<!--(.*?)-->',html,re.DOTALL)
# data=text[-1]
# final=re.findall('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+',data)
# final_text=''.join(final)
# print(final_text)
#

items = ['hello','fjeoijf','iofejo','jsfoej','final']
item1,*_,last = items
print(item1,last)

#coding:utf-8
from urllib2 import urlopen

html = urlopen("http://google.com").read()
print html

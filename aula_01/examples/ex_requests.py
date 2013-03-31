#coding:utf-8
import requests

html = requests.get("http://google.com").content
print html

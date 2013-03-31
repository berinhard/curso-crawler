#coding:utf-8
from lxml import etree
from lxml.html import HTMLParser

html_content = """
<html>
  <body>
    <h1>Example</h1>
    <ul>
        <li>First</li>
        <li>Second</li>
    </ul>
  </body>
</html>
""".strip()

parser = HTMLParser()
root = etree.fromstring(html_content, parser=parser)
print 'Todo html: ' + etree.tostring(root)
print '\nValores de li: '
for li in root.findall('.//li'):
    print li.text

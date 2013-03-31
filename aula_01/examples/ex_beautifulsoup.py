#coding:utf-8
from bs4 import BeautifulSoup

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

soup = BeautifulSoup(html_content)
print 'Todo html: ' + soup.prettify()
print '\nValores de li: '
for li in soup.find_all('li'):
    print li.string

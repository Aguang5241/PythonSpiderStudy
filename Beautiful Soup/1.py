html = '''
<html><head><title>This is a title</title></head>
<body>
<p class="title" name="Demo"><b>This is a Demo</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie-->></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
# 获取完整补全内容
print(soup.title)
# <title>This is a title</title>
print(type(soup.title))
# <class 'bs4.element.Tag'>
print(soup.title.string)
# This is a title
print(soup.title.name)
# title
print(soup.head)
# <head><title>This is a title</title></head>
print(soup.p)
# 只匹配第一个p标签
# <p class="title" name="Demo"><b>This is a Demo</b></p>
print(soup.p.attrs)
# {'class': ['title'], 'name': 'Demo'}
print(soup.p.attrs['name'])
# Demo
print(soup.p['name'], soup.p['class'])
# Demo ['title']
print(soup.head.title.string)
# 嵌套调用
# This is a title
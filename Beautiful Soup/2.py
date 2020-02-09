html = '''
<html>
<head>
<title>This is a title</title>
</head>
<body>
<p class="story">
Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie<span>
</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.
</p>
<p class="story">...</p>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)
# 返回子节点的列表
print(soup.p.children)
# <list_iterator object at 0x0000004928F2CD68>
for i, child in enumerate(soup.p.children):
    print(i, child)
    # 返回上面子节点生成器中的内容
print(soup.p.descendants)
# <generator object Tag.descendants at 0x00000023E04590C0>
for i, child in enumerate(soup.p.descendants):
    print(i, child)
    # 返回上面子孙节点生成器的内容


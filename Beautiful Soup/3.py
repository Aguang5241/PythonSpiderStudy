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
</p>
<p class="story">...</p>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.a.parent)
# 返回直接父节点
print(soup.a.parents)
# <generator object PageElement.parents at 0x00000096FFD890C0>
print(list(enumerate(soup.a.parents)))
# 返回上面祖先生成器中的内容
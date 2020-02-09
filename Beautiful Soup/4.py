html = '''
<html>
<body>
<p class="story">
Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie<span>
</a>
Hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.
</p>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.a.next_sibling)
# 返回下一个兄弟节点
print(soup.a.previous_sibling)
# 返回上一个兄弟节点
print(list(enumerate(soup.a.next_siblings)))
# 返回下面所有的兄弟节点
print(list(enumerate(soup.a.previous_siblings)))
# # 返回上面所有的兄弟节点
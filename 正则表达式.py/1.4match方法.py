'''
贪婪与非贪婪
'''
import re

content = 'Hello 1234567 World_This is a Regex Demo'

result1 = re.match('^He.*(\d+).*Demo$', content)
# .*采取贪婪匹配，只给（/d+）留下最后一个数字7
result2 = re.match('^He.*?(\d+).*Demo$', content)
# .*?采取非贪婪匹配，匹配全部1234567
print(result1, result2)
# <re.Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
print(result1.group(1), result2.group(1))
# 7 1234567

# 倘若需要匹配的内容在结尾，.*?会出现匹配不到对象的情况，此时.*符合要求
text = 'http://weibo.com/comment/kEraCN'
result3 = re.match('http.*comment/(.*?)', text)
result4 = re.match('http.*comment/(.*)', text)
print('>>>', result3.group(1), '>>>', result4.group(1))
# >>>  >>> kEraCN
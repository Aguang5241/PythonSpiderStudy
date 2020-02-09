import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
# 41

# ^匹配字符串的开头
# \s匹配任意空白字符，==[\t\n\r\f]; 
# \d匹配任意数字，==[0-9]; 
# {n}精准匹配n个前面的表达式; 
# \w匹配字母、数字及下划线的字符

result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)

print(result)
# <re.Match object; span=(0, 25), match='Hello 123 4567 World_This'>
print(result.group())
# Hello 123 4567 World_This
print(result.span())
# (0, 25)
import re

content = 'Hello 123 4567 World_This is a Regex Demo'

# .*代表匹配任意字符，用以简化正则表达式的书写
result = re.match('^Hello.*Demo$', content)

print(result)
# <re.Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
print(result.group())
# Hello 123 4567 World_This is a Regex Demo
print(result.span())
# (0, 41)
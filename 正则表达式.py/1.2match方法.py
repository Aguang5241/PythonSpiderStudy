import re 

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld', content)

print(result)
# <re.Match object; span=(0, 19), match='Hello 1234567 World'>
print(result.group())
# Hello 1234567 World
print(result.group(1))
# 1234567
print(result.span())
# (0, 19)
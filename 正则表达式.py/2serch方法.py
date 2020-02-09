'''
弥补match方法指定开头的限制
'''
import re

content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result.group(1))
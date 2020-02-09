'''
修饰符：
re.S---使.匹配包括换行符在内的字符
re.I---使匹配对大小写不敏感
re.M---做本地化识别（locale-aware）匹配
re.U---根据Unicode字符集解析字符
re.X---给予你更灵活的格式以便所写的正则表达式更易于理解
'''
import re

content = '''Hello 1234567 World_This 
is a Regex Demo
'''
result1 = re.match('^He.*?(\d+).*?Demo$', content)
 # print(result.group(1))
 # 报错，因为.*?匹配不到换行符
result2 = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result2.group(1))

'''
类似于字符串replace()方法，但是更强大
'''
import re

content = '1saffdsaf23dsaf45fdsa6fdsa789rewqr'
content = re.sub('[a-z]', '', content)
print(content)
# 123456789
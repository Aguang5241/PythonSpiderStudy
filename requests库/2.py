import requests

r = requests.get('http://httpbin.org/get')
print(r.text)

data = {
    'name': 'germey',
    'age': 22
}

r_1 = requests.get('http://httpbin.org/get', params=data)
print(r_1.text)
# 直接返回结果，得到字典格式
print(r_1.json())
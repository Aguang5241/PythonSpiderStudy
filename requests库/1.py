import requests



r = requests.get('https://baidu.com/')
# r = requests.post('http://baidu.com/')
# r = requests.put('http://baidu.com/')
# r = requests.delete('http://baidu.com/')
# r = requests.head('http://baidu.com/')
# r = requests.options('http://baidu.com/')
print(type(r))
print('>' * 30)
# 类型<class 'requests.models.Response'>
print(r.status_code)
print('>' * 30)
# 状态码200
print(type(r.text))
print('>' * 30)
# 响应体类型<class 'str'>
print(r.text)
print('>' * 30)
# 响应体neir
print(r.cookies)
print('>' * 30)
for key, value in r.cookies.items():
    print(key + '=' + value)
    print('>' * 30)
# cookies
print(type(r.headers), r.headers)
print('>' * 30)
# 获取响应头
print(type(r.url), r.url)
print('>' * 30)
# 获取url：http://baidu.com/
print(type(r.history), r.history)
print('>' * 30)
# 获取请求历史
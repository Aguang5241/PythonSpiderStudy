import requests

r0 = requests.get('http://www.baidu.com')
print('响应失败') if not r0.status_code == requests.codes.ok else print('成功响应')
r1 = requests.get('http://www.jianshu.com')
print('响应失败') if not r1.status_code == requests.codes.ok else print('成功响应')
import urllib.request

url = 'https://www.whatismyip.com/'

# 参数是一个字典{‘类型’：‘代理ip：端口号’}
proxy_support = urllib.request.ProxyHandler({'http':'103.53.168.169:9999'})
# 定制、创建一个opener
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400')]
# 安装一个opener
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

if '103.53.168.169' in html:
    print(1)
else:
    print(0)
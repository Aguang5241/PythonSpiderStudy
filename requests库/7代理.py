import requests 

proxies = {
    'http': 'http://10.10.1.10:3128',
    'http': '',
    'http': '',
    'http': '',
    'http': '',
}

requests.get ('http://baidu.com', proxies=proxies) 
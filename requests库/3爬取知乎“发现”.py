import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400'
}

r = requests.get('https://www.zhihu.com/special/all', headers = headers)
pattern = re.compile('data-za-detail-view-id.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
for title in titles:
    print(title)
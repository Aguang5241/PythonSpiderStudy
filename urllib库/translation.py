import urllib.request
import urllib.parse
import json
import time

while True:
    content = input('请输入需要翻译的内容（输入q退出程序）：')
    if content == 'q':
        break

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400'

    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15658686268937'
    data['sign'] = 'ee53369f775bc53f8be7328d3afb3631'
    data['ts'] = '1565868626893'
    data['bv'] = 'b9bd10e2943f377d66e859990bbee707'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTlME'

    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url, data, head)
    print(req.headers)

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    print('翻译结果：%s' % target['translateResult'][0][0]['tgt'])
    time.sleep(3)

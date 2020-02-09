from urllib.request import ProxyHandler, build_opener
import urllib.error
import socket

def main():
    # size = []
    max_try_time = 5
    i = 0
    for width in range(500, 1000):
        for height in range(100, 1000):
            if width % 50 == 0 and height % 50 == 0:
                # size.append([width, height])
                url = 'http://placekitten.com/%s/%s' % (width, height)
                proxy_handler = ProxyHandler({
                    

                })
                opener = build_opener(proxy_handler)

                for tries in range(max_try_time):
                    try:
                        req = opener.open(url, timeout=5)
                        req.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400')]
                    except urllib.error.HTTPError as e:
                        print(e.reason, e.code, e.headers, sep = '\n')
                    except urllib.error.URLError as e:
                        print(type(e.reason))
                        if isinstance(e.reason, socket.timeout):
                            print('>>>time out--try %d times' % (tries+1))
                    else:
                        img = req.read()
                        with open(r"C:/Users/Administrator/Desktop/png/cat_%dx%d.jpg" % (width, height), 'wb') as f:
                            f.write(img)
                        i += 1
                        print('>>>ok_%d--try %d times' % (i, tries+1))
                        break

if __name__ == '__main__':
    main()
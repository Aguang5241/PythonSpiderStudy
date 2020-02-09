import urllib.request
import chardet

def main():
    with open ('网站.txt', 'r') as f:
        urls = f.read().splitlines()

    for url in urls:
        response = urllib.request.urlopen(url)
        html = response.read()
        encode = chardet.detect(html)['encoding']
        

        filename = '%s.html' % url[7:]
        with open(filename, 'w', encoding = encode) as f_new:
            f_new.write(html.decode(encode, 'ignore'))

if __name__ == '__main__':
    main()
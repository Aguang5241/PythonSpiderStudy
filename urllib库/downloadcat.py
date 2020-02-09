import urllib.request

response = urllib.request.urlopen('http://placekitten.com/200/300')
cat_img = response.read()

#with open("cat_500x600.jpg", 'wb') as f:
#    f.write(cat_img)

print(response.geturl())
# 返回http://placekitten.com/200/300
print(response.info())
# 返回如下内容
# Date: Thu, 15 Aug 2019 11:25:30 GMT
# Content-Type: image/jpeg
# Transfer-Encoding: chunked
# Connection: close
# Set-Cookie: __cfduid=d1513a446acb36ffb52231d4922e2cef91565868330; expires=Fri, 14-Aug-20 11:25:30 GMT; path=/; domain=.placekitten.com; HttpOnly
# Access-Control-Allow-Origin: *
# Cache-Control: public, max-age=86400
# Expires: Fri, 16 Aug 2019 11:25:30 GMT
# CF-Cache-Status: HIT
# Age: 78936
# Vary: Accept-Encoding
# Server: cloudflare
# CF-RAY: 506acee85f33c785-AMS
print(response.getcode())
# 返回200状态码
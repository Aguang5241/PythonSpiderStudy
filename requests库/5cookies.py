import requests

headers = {
    'Cookies': '_zap=6ea5abd7-1f06-43de-912d-688125ad112e; d_c0="AOBjO7t60w-PTuwi1winsgcRRRmLwYvy5-c=|1564670181"; _xsrf=mmuY1r9k1DuYasCINj5zo1bMFyp7XHlL; capsion_ticket="2|1:0|10:1565923924|14:capsion_ticket|44:MWJjNGY1NmI4YWQ0NGQ2MmJlZDNmOTUzYTUxZDJkMTQ=|76f2d86cd88231d61522b86d66bca7e9c5dd2f9e7f9ac1d16171d506703373fd"; r_cap_id="MjU3ODI1NDE2Njg3NGJjNThmMzRiNzBhMmRkNzA3ZGQ=|1565924268|3fece6426114232a22d6ddb9dd7d5421146f7e6e"; cap_id="ZWU3MjdlMTg4ODkxNGI3OTg4NGQ0M2VjZWQ3MWNjOGM=|1565924268|0aff32c817abc86cfc01364ddc5d2248cab48bc8"; l_cap_id="MDczN2ZlZTQ2M2ZiNDBmMmJjNTZjZjgwMTgzNDhjODk=|1565924268|aec6528ff0c3f23457ce4a6204fd1b258caa4c93"; z_c0=Mi4xcGQ5Q0FnQUFBQUFBNEdNN3UzclREeGNBQUFCaEFsVk50V2xEWGdDR0I5Z2VPY19sQnN5Z3FSOGk0UWtoUFdxZVNR|1565924277|b5da5f50e42d5fb2b08e8cf3a239ce9f8c940a22; tst=r; tgw_l7_route=73af20938a97f63d9b695ad561c4c10c; BAIDU_SSP_lcr=https://www.baidu.com/link?url=We7ODk6Xv7nQmzcKuz1R5YeOssPhSeEA7KaytiZALem&wd=&eqid=af1158f6002b7574000000035d56b26d',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36'
}

r = requests.get('https://www.zhihu.com', headers = headers)
print(r.text)

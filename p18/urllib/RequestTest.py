# @author page
# @date 2017/11/28
# coding:utf-8
#!/usr/bin/python 

import urllib.request

def getUrlInfo(url,data,headers):
    req = urllib.request.Request(url,data,headers)
    print('full url',req.full_url)
    print('host:',req.host)
    print('data:',req.data)

if __name__ == '__main__':
    url = 'http://www.baidu.com/s'
    values = {'wd':'python'}
    data = urllib.parse.urlencode(values)
    data = data.encode(encoding = 'UTF8')
    headers = {'User-Agent':'Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)'}
    getUrlInfo(url,data,headers)

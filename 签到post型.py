#!./usr/bin/env.python
#.-*- coding: utf-8 -*-
#._author_.=."Max丶"
#.Date:.2019/2/21

import requests,json
from urllib import request

url = 'https://www.xxxx.zone/plugin.php?id=dc_signin:sign&inajax=1'

cookies = ''' _ga=GA1.2.9868781.1549185176; _gid=GA1.2.1102266281.1550761811; dyHK_2132_saltkey=pz66S604; dyHK_2132_lastvisit=1550760474; dyHK_2132_auth=eb49BfVj1tEasIbKr12LIid5U9aAfiU5eesj79cPNgbyZdBnU6kYKDnz5RpAFaScTWNTeiRZfxxxxxxxxxxxxxxxxxxxxxxxx'''

data = {
    'formhash':'1ca1c503',
    'signsubmit':'yes',
    'handlekey':'signin',
    'emotid':'9',
    'referer':'%E4%B8%8D%E5%BF%85%E8%BD%AC%E5%A4%B4%E5%B0%B1%E5%8F%AF%E4%BB%A5%E7%9C%8B%E7%9A%84%E7%AC%91%E8%84%B8%E3%80%82%E6%88%96%E6%98%AF%E4%B8%80%E5%8F%AA%E5%8F%AF%E7%88%B1%E7%9A%84%E5%B0%8F%E4%B8%8D%E7%82%B9%7E%7E'
}
headers = {
    'request':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    # 'cookie':cookie
}


def extract_cookies(cookies):
    """从浏览器或者request headers中拿到cookie字符串，提取为字典格式的cookies"""
    cookies = dict([l.split("=", 1) for l in cookies.split("; ")])
    return cookies

test = requests.post(url,headers=headers,data=data,cookies=extract_cookies(cookies))
# test2=request.urlopen(test)
# print(test.read().decode('utf-8'))
print(test)


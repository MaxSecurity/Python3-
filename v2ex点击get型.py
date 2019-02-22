#!./usr/bin/env.python
#.-*- coding: utf-8 -*-
#._author_.=."Max丶"
#.Date:.2019/2/21


import requests,time,datetime

url = 'https://www.v2ex.com/mission/daily/redeem?once=708xx'


cookie = '''_ga=GA1.2.1964354865.1548564927; PB3_SESSION="2|1:0|10:1550585042|11:PB3_SESSION|40:djJleDoxMTcuODcuMjAyLjE1MDo1Mzc5MzcyMA==|84bb090639b2191cff82b5c7527f58072b63f0de0fe67e318fdd78f9c5fa9e52"; _gid=GA1.2.1908952041.1550744900; V2EX_LANG=zhcn; _gat=1; A2="2|1:0|10:1550809262|2:A2|56:YjBkNTJjNmMwNjRiMTQ1YjQ5YzkyNTVkZGY3N2NmZTAwMjYyNjVjYw==|0016b6dd226b05dcaeea85c756aef38bf3a6fc10d27c37f02d234a16dee8bff8"; V2EX_TAB="2|1:0|10:1550809263|8:V2EX_TAB|8:dGVjaA==|08ee9da46ef2a4203b0576e3cadc7c3030c86edbcb84890314ecce12b74c8e9f"'''


headers = {
    'request':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    # 'cookie':cookie,
}

def extract_cookies(cookies):
    """从浏览器或者request headers中拿到cookie字符串，提取为字典格式的cookies"""
    cookies = dict([l.split("=", 1) for l in cookies.split("; ")])
    return cookies

def qiandao():
    qiandao=requests.get(url,headers=headers,cookies=extract_cookies(cookie))#带上headers和cookie信息打开url
    # test2=request.urlopen(签到)  这个是另一种写法！
    time.sleep(2)#延时两秒


#定时签到每天在12点时候
def main(h=12, m=00):
    while True:
        now = datetime.datetime.now()
        if now.hour == h and now.minute == m:
            qiandao()
            # print 1
        # 每隔60秒检测一次
        time.sleep(60)


main()



from urllib import parse
from urllib import request
from urllib import error
import http.cookiejar
import http
import unicodedata
import string
import re
# values = {'username': '945558695@qq.com', 'password': '52wpy130wpy'}
# data = parse.urlencode(values).encode(encoding='UTF8')
# url = "https://mail.qq.com"
# headers = {"user-Agent": "Mozilla", "Referer": "http://www.baidu.com"}
# req = request.Request(url, data)
# html = request.urlopen(req)
# print(html.read())

# req = request.Request("http://www.xxx.com")
# try:
#     request.urlopen(req)
# except error.URLError as e:
#     print("Error Reason: ", e.reason)
# req = request.Request("http://blog.csdn.net/cqcre")
# try:
#     request.urlopen(req)
# except error.HTTPError as e:
#     print("Error Code: ", e.code)

# cookie = http.cookiejar.CookieJar()
# handler = request.HTTPCookieProcessor(cookie)
# openner = request.build_opener(handler)
# response = openner.open("http://www.baidu.com")
# for item in cookie:
#     print("Name="+item.name)
#     print("Value"+item.value)

# filename = "cookie.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# reponse = opener.open("http://www.baidu.com")
# cookie.save(ignore_discard=True, ignore_expires=True)

# cookie = http.cookiejar.MozillaCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# req = request.Request("http://www.baidu.com")
# opener = request.build_opener(request.HTTPCookieProcessor(cookie))
# reponse = opener.open(req)
# print(reponse.read())

#生成cookie保存下来，并使用
# filename = "cookie.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)
# opener = request.build_opener(request.HTTPCookieProcessor(cookie))
# data = {"id": "SX1605101", "password": "19940130"}
# data = parse.urlencode(data).encode(encoding='UTF8')
# url = "http://gsmis.nuaa.edu.cn/pyxx/login.aspx"
# response = opener.open(url, data)
# cookie.save(ignore_discard=True, ignore_expires=True)
# url2 = "http://gsmis.nuaa.edu.cn/pyxx/Default.aspx"
# response = opener.open(url2)
# print(response.read())

# import re
# pattern = re.compile(r'hello')
# result1 = re.match(pattern, 'hello')
# result2 = re.match(pattern, 'helloo cqc')
# result3 = re.match(pattern, 'helo cqc')
# result4 = re.match(pattern, 'hello cqc')
# if result1:
#     print(result1.group())
# else:
#     print('1匹配失败')
# if result2:
#     print(result2.group())
# else:
#     print('2匹配失败')
# if result3:
#     print(result3.group())
# else:
#     print('3匹配失败')
# if result4:*
#     print(result4.group())
# else:
#     print('4匹配失败')


page = 1
url = 'http://www.qiushibaike.com./hot/page/' + str(page)
#Usr-Agent主要就是包括: 浏览器名和版本号，操作系统名和版本号，默认语言
user_agent = 'Mozilla/4.0(compatible; MISE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    buf = response.read()
    buf = buf.decode('utf-8')
    # buf.replace('<br/>', '/n')
    # print('开始')
    # print(buf)
    pattern = re.compile(r'<div class="content">.*?<span>(.*?)</span>', re.S)
    items = re.findall(pattern, buf)
    for index, item in enumerate(items):
        print('%d:\n%s\n' % (index, item))
except error.HTTPError as e:
    if hasattr(e, 'code'):
        print('Error code: ', e.code)
    if hasattr(e, 'reason'):
        print('Error Reason: ', e.reason)




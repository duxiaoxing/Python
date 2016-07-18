# coding:utf-8
# Python爬虫学习c
# Urllib 库的基本使用


# import urllib
# import urllib2
#
# request = urllib2.Request("http://www.baidu.com")
# response = urllib2.urlopen(request)
# print response.read()

# import urllib
# import urllib2
#
# values = {}
# values['username'] = "1016903103@qq.com"
# values['password'] = "XXXX"
# data = urllib.urlencode(values)
# url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# print request.get_full_url()
# # print response.read()

# import urllib
# import urllib2
#
# from urllib import urlopen
# from urllib import unquote
#
# values = {}
# values['username'] = "1016903103@qq.com"
# values['password'] = "XXXX"
# data = urllib.urlencode(values)
# url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url + '?'+data)
# response = urllib2.urlopen(request)
# print request.get_full_url()
# print unquote(data)
# print response.read()



# import urllib2
#
# # usr_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
# # headers = {'User-Agent': usr_agent}
# # req = urllib2.Request('http://blog.csdn.net/cqcre', '', headers)
# req = urllib2.Request('http://blog.csdn.net/cqcre')
# try:
#     print urllib2.urlopen(req).read()
#
# except urllib2.HTTPError, e:
#     print e.code
#     print e.reason

# 保存cookie
# import urllib2
# import cookielib
#
# # # 声明一个CookieJar对象实例来保存cookie
# # cookie = cookielib.CookieJar()
# # # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# # handler = urllib2.HTTPCookieProcessor(cookie)
# # # 通过handler来构建opener
# # opener = urllib2.build_opener(handler)
# # # 此处的open方法同urllib2的urlopen方法，也可以传入request
# # response = opener.open('http://www.baidu.com')
# # for item in cookie:
# #     print 'Name = ' + item.name
# #     print 'Value = ' + item.value
#
# # 设置保存cookie的文件，同级目录下的cookie.txt
# filename = 'cookie.txt'
# # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# opener = urllib2.build_opener(handler)
# # 创建一个请求，原理同urllib2的urlopen
# response = opener.open("http://www.baidu.com")
# # 保存cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)

# 读取cookie
import cookielib
import urllib2

# 创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 创建请求的request
req = urllib2.Request("http://www.baidu.com")
# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()




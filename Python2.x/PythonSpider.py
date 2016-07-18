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

# # 读取cookie
# import cookielib
# import urllib2

# # 创建MozillaCookieJar实例对象
# cookie = cookielib.MozillaCookieJar()
# # 从文件中读取cookie内容到变量
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# # 创建请求的request
# req = urllib2.Request("http://www.baidu.com")
# # 利用urllib2的build_opener方法创建一个opener
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read()

# 爬糗事百科帖子
# # coding:utf-8 
# import urllib
# import urllib2
# import re

# url = 'http://www.qiushibaike.com/'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = { 'User-Agent' : user_agent }
# try:
#     request = urllib2.Request(url,headers = headers)
#     response = urllib2.urlopen(request)
#     # print response.read()
# except urllib2.URLError, e:
#     if hasattr(e,"code"):
#         print e.code
#     if hasattr(e,"reason"):
#         print e.reason  
# content = response.read().decode('utf-8')
# pattern = re.compile('<div.*?class="article block untagged mb15>',re.S)
# items = re.findall(pattern,content)
# for item in items:
#     print item[0],item[1],item[2],item[3],item[4]  


# coding=utf-8
import urllib
import urllib2
import re
import thread
import time

class QSBK:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        self.headers = {'User-Agent' :self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url,headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print "error",e.reason
                return None

    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "page load error"
            return None
        pattern = re.compile('<h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</',re.S)
        items = re.findall(pattern,pageCode)
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip(),item[2].strip()])
        return pageStories

    def loadPage(self):
        if self.enable==True:
            if len(self.stories)<2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex +=1

    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "Q":
                self.enable = False
                return
            print u"第%d页\t发布人：%s\t 赞：%s\n%s" %(page,story[0],story[2],story[1])

    def start(self):
        print u'正在读取，回车查看，Q退出'
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage +=1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()


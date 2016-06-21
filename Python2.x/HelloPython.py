# encoding: utf-8
# 廖雪峰博客地址:http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000
# print "Hello Python"


# print 'The quick brown fox','jumps over','the lazy dog'

# !/usr/bin env python
# print 100+200
# print '100+200'

# name = raw_input()
# # print'输入的名字是',name
# print'Hello', name

# print absolute value of an integer:
# a = 100
# if a >= 0:
#     print a
# else:
#     print -a

# a = input()
# print '仅支持输入数字', '用户输入是', a
# if a >= 0:
#     print a
# else:
#     print -a

# a = ord('A');
# print a;

# a = chr(65);
# print a;

# print u'中文'

# s =  u'中文'.encode('utf-8')
# print s;
# print len(s);
# print 'ABC的长度是:' ,len('ABC');

# print '中文' ,len(u'中文');
# print '中文GBK' ,len(u'中文'.encode('utf-8'));

# HelloString = 'Hello %s' % 'world';
# print HelloString;

# HelloString = 'Hi, %s, you have $%d.' % ('Michael', 1000000);
# print HelloString;

# HelloString = u'Hi ,%s' % (u'Michael');
# print HelloString;

# nameList = ['John','Jim'];
# nameList.insert(0,'index2');
# nameList.append('0');
# nameList.append(1);
# print nameList;
# print len(nameList);
# print nameList[-2];

# age = raw_input()
# if age > 18:
#     print 'your age is ',age
#     print '成年'
# else:
#     print 'your age is', age
#     print 'teenager'

# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum + x
# print sum

# sum = 0
# for x in range(101):
#     sum += x;
# print sum;

# array = range(101);
# for index in range(len(array)):
#     print array[index];

# info = {
#     'name':'john'
# }
# info.pop('name');
# info.setdefault('age':2)
# print info;

# def my_abs(x):
#     if not isinstance(x,(int,float)):
#     raise TypeError('类型错误')
#     if x >= 0:
#         return x
#     else:
#         return -x

# print my_abs(-199)
# print my_abs('a')


# import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny

# # x, y = move(100, 100, 60, math.pi / 6);
# # print x, y
# r = move(100, 100, 60, math.pi / 6)
# print r

# def enroll(name, gender):
#     print 'name:', name
#     print 'gender:', gender

# enroll('Jim','F')

# def enroll(name, gender, age=6, city='Shenzhen'):
# 	print 'name:', name
# 	print 'gender:', gender
# 	print 'age:', age
# 	print 'city:', city

# enroll('Sarah','F')

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L

# add_end();
# print add_end()
# print add_end()

# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum

# print calc([1, 2, 3])
# print calc([])

# def person(name, age, **kw):
#     print 'name:', name, 'age:', age, 'other:', kw

# kw = {'city': 'Beijing', 'job': 'Engineer'}
# # print person('Jack', 24, city=kw['city'], job=kw['job'])
# print  person('Jack', 24, **kw)


# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
# print fact(5)

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print L[0:len(L)]

# from collections import Iterable

# L = range(100);
# print L[0::5]

# print isinstance(L,Iterable)

# print [x * x for x in range(1, 11)]
# print [x * x for x in range(2,11,2)]

# print [m + n for m in 'ABC'  for n in 'EFG']

# import os
# print  [d for d in os.listdir('.')]

# g = (x * x for x in range(1,10,1))
# while g.next():
#     print g.next()
# # print g.next()

# def fbi(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print b
#         a,b = b, a + b
#         n = n + 1

# fbi(6)


# def fbi(max):
#     n,a,b = 0,0,1
#     while n < max:
#         yield b
#         a,b = b, a + b
#         n = n + 1

# for n in fbi(6):
#     print n

# f = abs
# print f(-10)

# def fn(x, y):
#     return x * 10 + y

# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


# def upder(s):
#     return {'a':'A'}[s]

# print map(upder,'aaa')
# print map(char2num,'13579')

# print reduce(fn, map(char2num, '13579'))

# print sorted(['bob', 'about', 'Zoo', 'Credit'])


# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#
#     return sum
#
#
# f = lazy_sum(1, 3, 5, 7, 9)
# print f
# print f()

# 闭包函数
# def count():
#     fs = []
#     for i in range(1, 4, 1):
#         def f():
#             return i * i
#
#         fs.append(f)
#     return fs

# def count():
#     fs = [];
#     for i in range(1, 4):
#         def f(j):
#             def g():
#                 return j * j
#
#             return g
#
#         fs.append(f(i))
#     return fs
#
#
# f1, f2, f3 = count()
# print f1, f2, f3
# print f1(), f2(), f3()

# # 匿名函数
# print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# 装饰器
# def now():
#     print '2016-06-20'
#
# f = now
# f()

# def log(func):
#     def wapper(*args, **kwargs):
#         print 'call_func_name: %s()' % func.__name__
#         return func(*args, **kwargs)
#
#     return wapper
#
#
# @log
# def now():
#     print '2016-06-20'
#
#
# now()

# def now():
#     print '2016-06-20'
#
#
# now = log(now)
# now()

# 偏函数
# print int('123456')
# print int('123456', base=8)
# print int('123456', 8)


# def int2(x, base=2):
#     return int(x, base)
#
#
# print int2('1000000')

# import functools
#
# int2 = functools.partial(int, base=2)
# print int2('1000000')

# 模块
# 使用模块

# import sys
# args = sys.argv
# print args

# 面向对象

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print 'name:%s score:%s ' % (self.name, self.score)
#
#
# Bob = Student('Bob', 99)
# Bob.print_score()


# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print '%s: %s' % (self.name, self.score)
#
# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()

# 使用 property
# class Student(object):
#     @property
#     def score(self):
#         return self.score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer !')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 - 100 !')
#         self.score = value
#
# #
# s = Student()
# # s.score = 60
# # print  s.score
# s.score = 999
# print s

class Man(object):
    def __init__(self):
        self.birth = 0

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2016 - self._birth


m = Man()


# print m.age
# m.birth = 1991
# print m.age
#
# print dir(Man)
# print m.__dict__
# print Man.__dict__


# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1  # 初始化两个计数器a，b
#
#     def __iter__(self):
#         return self  # 实例本身就是迭代对象，故返回自己
#
#     def next(self):
#         self.a, self.b = self.b, self.a + self.b  # 计算下一个值
#         if self.a > 100000:  # 退出循环的条件
#             raise StopIteration();
#         return self.a  # 返回下一个值
#
#
# for n in Fib():
#     print n


# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
# f = Fib()
#
# print f[1]
# print f[2]
# print f[3]

# print range(100)[5:10]

# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#     #
#     def __str__(self):
#         return self._path
# print Chain().status.user.timeline.list

import os
# print os.name
# print os.uname()
# print os.environ
# print os.getenv('PATH')



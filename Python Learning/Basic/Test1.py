#-*- coding:utf-8 -*-
#如果代码中有中文，则代码文件中第一行必须为
#coding=utf-8或#coding:utf-8或#-*- coding:utf-8 -*-否则会报如下错误
'''
File "test1.py", line 3
SyntaxError: Non-ASCII character '\xe5' in file test1.py on line 3, but no encod
ing declared; see http://python.org/dev/peps/pep-0263/ for details
'''
from __future__ import division
import math
from math import sqrt
import cmath #引入虚数概念
print 1/2 #利用future这个特性，证明1/2不为0

#导入精确除法后，若要执行截断除法，可以使用"//"操作符：
print 3/4  #0.75
print 3//4 #0 //双斜线实现整除
print 3.0//4.0
#取余
print 10%3
#求幂
print 2**3
print pow(2,4)
print pow(2,4,15)#相当于(2**4)%15
"""
    pow(x, y[, z]) -> number

    With two arguments, equivalent to x**y.  With three arguments,
    equivalent to (x**y) % z, but may be more efficient (e.g. for longs).
    """
print 10+pow(2,3*5)/3.0
print abs(-10)#取绝对值
print round(1.0/2.0)#四舍五入后取最接近的整数值
#floor取小于该数的最大整数
print math.floor(32.9)
print int(math.floor(32.9))
#cell取大于该数的最小整数
print math.ceil(32.9)
print int(math.ceil(32.9))
#不用直接写模块名
print sqrt(9)
#通过对变量来引用函数
foo=math.sqrt
print foo(16)
#引入虚数
print cmath.sqrt(-1)
print (1+3j)*(9+4j)
#if语句
minutes=60
if minutes%60==0:print 'time is dead'
else:print'time not dead'
#获得用户输入
user_name=raw_input("what is your name?")
print "hello ,"+user_name+" !"
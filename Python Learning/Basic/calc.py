#-*- coding:utf-8 -*-
#如果代码中有中文，则代码文件中第一行必须为
#coding=utf-8或#coding:utf-8或#-*- coding:utf-8 -*-否则会报如下错误
'''
File "test1.py", line 3
SyntaxError: Non-ASCII character '\xe5' in file test1.py on line 3, but no encod
ing declared; see http://python.org/dev/peps/pep-0263/ for details
'''
from __future__ import division

print 1/2 #利用future这个特性，证明1/2不为0

#导入精确除法后，若要执行截断除法，可以使用"//"操作符：
print 3/4  #0.75
print 3//4 #0
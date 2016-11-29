#coding=utf-8
'''
@author: mrye
@Create date: 2016-11-15
@description: 循环下载文件  
@Update date: 2016-11-15
'''

import urllib 
import urllib2 
import requests

def log_file(content,flag):
	if flag==1:
		f=open('success.txt','a')
		f.write(content+'\n')
	elif flag==0:
		f=open('failure.txt','a')
		f.write(content+'\n')
	f.close()

def test_download(url,name):
	req = urllib2.Request(url)
	req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36')
	f = urllib2.urlopen(req)
	#f = urllib.urlopen(url)
	if "Content-Length" in f.info():
		urllib.urlretrieve(url, name)
		log_file(url+'\n'+str(f.info()),1);
	else:
		print f.getcode()
		print f.info()
		log_file(url+'\n'+str(f.info()),0);

'''
主函数
测试用例:http://www.test.com/22.rar
'''
if __name__=="__main__":
	#for num in range(1,20):
	num=14
	while(num<=20):
		filename=str(num)+'_1.rar'
		print "Start::==>>http://www.test.com/"+filename
		url = "http://www.test.com/"+filename
		test_download(url,filename)
		print "END::==>>......................."
		num=num+1
	pass



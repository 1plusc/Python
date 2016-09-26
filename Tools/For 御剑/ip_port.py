#coding:utf-8
# Author:MRYE
# Date:2016-09-26 23:17
# Github:https://github.com/1plusc
#根据御剑扫描日志整理如IP:Port格式如(10.10.10.10:8080)
f = open("PortScan-100.txt", "r")
fin=open(r'all_IP_Port.txt','w')
IP="0.0.0.0"
NUM=3
PORT=0
NUMBER=0
COUNT=0
FLAG=False
FLAG_IP=True
'''
获取端口号
'''
def getport(str):
	temp=""
	str=str.strip()
	if str=='\r\n'or str=='':
		"空行"
	else:
		for i in str:
			if i.isdigit():
				temp+=i
			else:
				break
	return temp;

'''
判断字符串是否为IP,方法为内容是否含英文字母
'''
def judge_IP(str):
	for c in str:
		if c.isalpha():
			return False
	return True
'''
根据行内数据判断IP OR PORT
'''
def printme( str ):
	"获取IP与端口"
	global IP
	global PORT
	global COUNT
	global FLAG
	global NUMBER
	COUNT=str.count(".")
	FLAG_IP=judge_IP(str)
	if COUNT== NUM and FLAG_IP:
		IP=str
		NUMBER+=1
		FLAG=False
	else:
		PORT=getport(str)
		FLAG=True
	return;
'''
主程序
'''
while True:
    line = f.readline()  
    if line:
		line=line.strip()
		printme(line)
		if FLAG:
			print "The IP Merge Port is :"+IP+":"+PORT
			fin.write(IP+":"+PORT+"\r\n")
		else:
			"此处预留"
    else:  
        break
fin.write("Here have "+str(NUMBER)+" IP ,thank you for use")
f.close()
fin.close()
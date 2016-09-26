#coding:utf-8
# Author:MRYE
# Date:2016-09-27 00:17
# Github:https://github.com/1plusc
#根据御剑扫描日志整理后的IP---如IP:Port格式如(10.10.10.10:8080)
#判断是否有效
import socket
fin=open('all_IP_Port.txt','r')
fout=open(r'allvalid_IP_Port.txt','w')
FLAG=False
def get_info(str):
	global FLAG
	strn=str.split(":")
	sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sk.settimeout(1)
	try:
		sk.connect(strn[0],strn[1])
		print 'Server port OK!'
		FLAG=True
	except Exception:
		print 'Server port not connect!'
		FLAG=False
	sk.close()

while True:
	line = fin.readline()
	print line
	print line[0]
	if line[0]!="H":
		line=line.strip()
		get_info(line)
		if FLAG:
			print "The IP Merge Port is :"+IP+":"+PORT
			fout.write(IP+":"+PORT+"\r\n")
		else:
			"此处预留"
	else:
		break

fin.close()
fout.close()
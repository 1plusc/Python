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
NUMBER=0
def get_info(str):
	global FLAG
	global NUMBER
	strn=str.split(":")
	sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sk.settimeout(1)
	try:
		if (int(strn[1])==80 or (int(strn[1])<=9000 and int(strn[1])>=8000)):
			print strn[1]
			sk.connect(strn[0],strn[1])
			print 'Server port OK!'
			FLAG=True
		else:
			FLAG=True
		NUMBER+=1
	except Exception:
		print 'Server port not connect!'
		FLAG=False
	sk.close()

while True:
	line = fin.readline()
	if line[0]!="H":
		line=line.strip()
		get_info(line)
		if FLAG:
			fout.write(line+"\r\n")
		else:
			"此处预留"
	else:
		break

fout.write("Here have "+str(NUMBER)+" Valid IP ,thank you for use")
fin.close()
fout.close()
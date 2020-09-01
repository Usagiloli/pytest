import socket
import sys

def tClient():
	s=socket.socket()
	addr=sys.argv[1]
	port=int(sys.argv[2])
	s.connect((addr,port))
	
	
	cmd:str=''
	for i in range(3,len(sys.argv)):
		cmd+=sys.argv[i]+' '
	bcmd=bytes(cmd,encoding="utf-8")
	s.send(bcmd)
	
	
	becho=s.recv(65535)
	echo=str(becho,encoding="utf-8")
	print(echo)
	s.close()
tClient()

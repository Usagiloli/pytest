import socket
import sys
import threading
import queue

try:
	host:str=sys.argv[1]
	sport=int(sys.argv[2])
	eport=int(sys.argv[3])
except:
	print("\n\n\nhost startport endport (threadNum=500) (q=0)\n\n\n")

try:
	if((sys.argv[5]=='q')or(sys.argv[5]=='1')):
		threadNum=int(sys.argv[4])
		sw=1#0==close progress echo 1==open
except:
		threadNum=500
		sw=0

#host='192.168.0.114'
#sport=100
#eport=500
#threadNum=50

q=queue.Queue()
for i in range(sport,eport):
    q.put(i)

#for port in range(sport,eport):
class PortScanner(threading.Thread):
    def run (self):
        while(1):
            port=q.get()
            self.scanner(host,port)
            q.task_done()
    def scanner(self,host,port):
        #print(port)
        self.progress(port,sw)
        s=socket.socket()
        try:
            s.connect((host,port))
            print((host,port),""" is open""")
            s.close()
        except:
            pass
    def progress(self,port,switch):
            if((port%threadNum==0)and(switch)):
                print("Scanning:",port)


for i in range(threadNum):
    t=PortScanner()
    t.setDaemon(True)
    t.start()

q.join()


print("ok")

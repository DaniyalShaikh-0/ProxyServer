from socket import *
import time
host='localhost'
port=1200
s=socket(AF_INET,SOCK_STREAM)
# s.settimeout(5)
s.connect((host,port))
modifiedMessage, serverAddress = s.recvfrom(2048)
modifiedMessage2, serverAddress2 = s.recvfrom(2048)
# modifiedMessage3, serverAddress3 = s.recvfrom(2048)
print (modifiedMessage.decode())
print (modifiedMessage2.decode())
# print (modifiedMessage3.decode())
time.sleep(2)
data=input()
s.send(data.encode('utf-8'))
print('....Sent')
s.close()
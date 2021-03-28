from os import startfile
from socket import *
from bs4 import BeautifulSoup
import time
class Server_proxy:
    prox_socket=None
    port=None
    host=None
    type_=None
    active_clients=[]
    startmsg=None
    def __init__(self,port,host,type_='T'):
        if type_=='U':
            self.prox_socket=socket(family=AF_INET,type=SOCK_DGRAM)
        else:
            self.prox_socket=socket(family=AF_INET,type=SOCK_STREAM)
        self.host=host
        self.port=port
        self.prox_socket.bind((self.host,self.port))
        self.prox_socket.listen(5)
    def make_live(self):
        # self.prox_socket.settimeout(10)
        client = self.prox_socket.accept()
        self.active_clients.append(client)
        self.startmsg='Welcome to proxy Server made my 18k1055 and 18k0163'
        client[0].send(self.startmsg.encode('utf-8'))
        time.sleep(1)
        client[0].send('enter your request : '.encode())
        c_data=client[0].recv(2048).decode()
        print('Clients data is: ',c_data)
        if c_data=='close':
            client[0].close()
        elif c_data=='CLOSE':
            self.prox_socket.close()
        # self.prox_socket.settimeout(None)
        # fileobj = self.prox_socket.makefile('rb', 0)
            
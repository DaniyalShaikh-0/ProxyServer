from Server import ServerSocket as SS
import sys
import os
hostname='localhost'
port=1200
print(sys.path)
NewServer=SS.Server_proxy(port,hostname)
while True:
    NewServer.make_live()
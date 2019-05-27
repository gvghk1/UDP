#Reference:
# 1. https://stackoverflow.com/questions/27893804/udp-client-server-socket-in-python
# 2. https://github.com/dtechcoach/UDP
# 3. My repo: https://github.com/gvghk1/UDP
        
#UDPClient.py
import time
from socket import socket, SOCK_DGRAM, AF_INET


#Set Server info and a UDP socket
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

#Set a timeout value of 1 second
clientSocket.settimeout(1)

message = raw_input('Input lowercase sentence: ')
#Send message to server
clientSocket.sendto(message, (serverName, serverPort))

#If data is back from server, print the message.
try:
    modifiedMessage, addr = clientSocket.recvfrom(2048)
    print modifiedMessage, addr

#If no data is back from server, print time out message
except timeout:
        print 'REQUEST TIMED OUT'

clientSocket.close()

#Allow the client to give up if no response has been reveived within 1 second.



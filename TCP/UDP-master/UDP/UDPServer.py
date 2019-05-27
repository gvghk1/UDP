#Reference:
# 1. https://stackoverflow.com/questions/27893804/udp-client-server-socket-in-python
# 2. https://github.com/dtechcoach/UDP
# 3. My repo: https://github.com/gvghk1/UDP

#UDPServer.py

#UDP (SOCK_DGRAM) is a datagram-based protocol. You send one 
#datagram and get one reply and then the connection terminates.
import random
from socket import socket, SOCK_DGRAM, AF_INET

#Create a UDP socket 
#Notice the use of SOCK_DGRAM for UDP packets
#AF_INET is the Internet address family for IPv4
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print "Waiting for connections"
while True:
        # Generate random number in the range of 0 to 10
        rand = random.randint(0, 10)
      
         # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(2048)
   
        # Capitalize the message from the client
        message = message.upper()
        print message, address
   
        # If rand is less is than 4, we consider the packet lost and do notrespond
        if rand < 4:
            continue
         
        serverSocket.sendto(message, address)
serverSocket.close()


#Configure the server so that it randomly drops packets.
#Include information about how long each response took. This will be the RTT.

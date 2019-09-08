#!/usr/bin/env python3
import socket
import random

ipAdd = socket.gethostbyname(socket.gethostname())
print(ipAdd)
# Set up our receiving socket
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.bind(("localhost", 7777))


# Receive, print, and echo data
data, address = udpSocket.recvfrom(512)
print("Received %s from %s on port %d" %(data, address[0], address[1]))
udpSocket.sendto(data, address) #echo

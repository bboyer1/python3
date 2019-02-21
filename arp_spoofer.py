#!/usr/local/bin/python3
#Boyer

#Description: To use against switches without port security
#Purpose: To gather information about the network

######DRAFT######


import netifaces

print(netifaces.ifaddresses('en0'))

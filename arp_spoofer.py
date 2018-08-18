#!/usr/bin/env python
#Boyer

#Description: To mess with switches without port security
#Purpose: To gather information about the network

######DRAFT######


import os
import uuid

print 'mac_address'

mac_address = hex(uuid.getnode())[2:-1]

#mac_address = mac_address

#mac_address = mac_address['O']
print mac_address

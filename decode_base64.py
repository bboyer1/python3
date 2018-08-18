#!/usr/bin/env python
#Boyer

#Description: To decode any base64 encoded device
#Purpose: To make CTFs quicker

import sys
import base64


text = sys.argv[1]
#text = 'helloworld'
#encoded_text = base64.b64encode(text)

decoded_text = base64.b64decode(text)


print decoded_text

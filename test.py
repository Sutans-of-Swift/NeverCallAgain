#! /usr/bin/env python3
import sys
import base64

body = str(base64.urlsafe_b64decode(sys.argv[1]), "utf-8")
print(body)

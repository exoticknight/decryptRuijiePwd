#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import sys
import base64

xorKey = "~!:?$*<(qw2e5o7i8x12c6m67s98w43d2l45we82q3iuu1z4xle23rt4oxclle34e54u6r8m"

print("".join(chr(ord(a) ^ ord(b)) for a, b in zip(base64.b64decode(sys.argv[1]), xorKey)))
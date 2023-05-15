from pwntools import *

msg = "label"

dec_msg = xor(msg)

print(dec_msg)

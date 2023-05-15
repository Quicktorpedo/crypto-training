#!/usr/bin/env python3

import base64

enc_msg = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

msg_bytes = bytes.fromhex(enc_msg)

msg_b64 = base64.b64encode(msg_bytes)

print(msg_b64.decode())


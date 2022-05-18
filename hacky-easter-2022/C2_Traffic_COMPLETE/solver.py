#!/usr/bin/env python3

from hashlib import sha256
from Crypto.Cipher import AES
from base64 import standard_b64decode,standard_b64encode
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Random.random import randint
from Crypto.Util.Padding import pad, unpad
import subprocess

def long_to_base64(n):
    return standard_b64encode(long_to_bytes(n)).decode()

def encrypt(cipher, msg):
    return standard_b64encode(cipher.encrypt(pad(msg, 16))).decode()

def base64_to_long(e):
    return bytes_to_long(standard_b64decode(e))

def decrypt(cipher, e):
    return unpad(cipher.decrypt(standard_b64decode(e)), 16)

cipher = None

def handle(j):
    global cipher
    if cipher is None:
        p = base64_to_long(j['p'])
        g = base64_to_long(j['g'])
        A = base64_to_long(j['A'])
        b = 620620105
        shared = pow(A, b, p)
        shared = sha256(long_to_bytes(shared)).digest()
        cipher = AES.new(shared, AES.MODE_ECB)
        return {
            'B': long_to_base64(pow(g, b, p))
        }

    cmd = decrypt(cipher, j['rpc'])
    print(cmd)
    return {
        'return': encrypt(cipher, subprocess.check_output(cmd))
    }

j={
            "p": "h3rl/Q==",
            "g": "Ag==",
            "A": "QpFOyA=="
        }

print(handle(j))

print(decrypt(cipher,"GkSU2VwQyFe5Jt0Vd0cfxw=="))

print(decrypt(cipher,"3eWXhpQagWGMlfc71Qxd2QMvy4EVIyLfP54Jm6lpyHot6Qz+U7t3q2DdKnOxZBQf"))

# Brute force  -  but this takes too long
# i=0
# while i<p:
#     if pow(g,i,p) == 1042188408:
#         print(i)
#         break

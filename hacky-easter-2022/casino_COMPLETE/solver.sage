#!/usr/bin/env sage
# -*- coding: utf-8 -*-

import os
os.environ['PWNLIB_NOTERM'] = '1'

import pwn
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad

# NIST P-256 curve
p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b

E = EllipticCurve(GF(p), [-3,b])
P = E.lift_x(15957832354939571418537618117378383777560216674381177964707415375932803624163)
Q = E.lift_x(66579344068745538488594410918533596972988648549966873409328261501470196728491)

# P = dQ
d = Q.discrete_log(P)

def do_next(s):
    sP = s * P
    r = Integer(sP[0])
    s_new = Integer((r * P)[0])
    rQ = r * Q
    return Integer(rQ[0]), s_new

def do_guess(r1):
    try:
        rQ1 = E.lift_x(r1)
    except ValueError:
        return None
    sp2 = d * rQ1
    s2 = Integer(sp2[0])
    r2, s3 = do_next(s2)
    return s3, r2

rem = pwn.remote("46.101.107.117",2212)
rem.recvline()
rem.recvuntil('Your id is ')
r1=rem.recvline()
r1=Integer(int(r1))

dict_i={}

for i in range(2 ** 8):
    print(i)
    r1_guess = (r1 << 8) + i
    guess = do_guess(r1_guess)
    if guess:
        s3, r2_guess = guess
        dict_i[i] = [s3, r2_guess>>8]

balance=10
while True:
    rem.recvuntil('> ')
    rem.sendline('p')
    rem.recvuntil('Your bet: ')
    rem.sendline('0')
    rem.recvuntil('Your current balance: ')
    new_balance = int(rem.recvline())
    if new_balance > balance:
        print("it was even")
        for i in list(dict_i):
            if dict_i[i][1] % 2 == 1:
                dict_i.pop(i)
    else:
        print("it was odd")
        for i in list(dict_i):
            if dict_i[i][1] % 2 == 0:
                dict_i.pop(i)
    for i in (list(dict_i)):
        print(i)
        s2=dict_i[i][0]
        r2_guess, s2 = do_next(s2)
        r2_guess = r2_guess>>8
        dict_i[i]=[s2, r2_guess]
    balance=new_balance
    print(len(dict_i))
    if len(dict_i) == 1:
        break
    if len(dict_i) == 0:
        exit("Something wrong!")
        break

for key in dict_i:
    print(key)

r2_guess, s2 = dict_i[key]
r2_guess = r2_guess>>8
bet = r2_guess % 2

while True:
    rem.recvuntil('> ')
    rem.sendline('p')
    rem.recvuntil('Your bet: ')
    rem.sendline(str(bet))
    rem.recvuntil('Your current balance: ')
    balance=int(rem.recvline())
    if balance == 1337:
        break
    s2=dict_i[key][0]
    r2_guess, s2 = do_next(s2)
    r2_guess = r2_guess>>8
    dict_i[key]=[s2, r2_guess]
    bet = r2_guess % 2

print(dict_i[key])

rem.recvuntil('> ')
rem.sendline('b')
cipher=rem.recvline()
print(cipher)
print(type(cipher))

def decrypt(r,cipher):
    """
    Decrypt the ciphertext from the challenge.
    """
    ct = bytes.fromhex(
        (str(cipher))[2:-3]
    )
    aes_key = SHA256.new(str(r).encode("ascii")).digest()
    cipher = AES.new(aes_key, AES.MODE_ECB)
    pt = cipher.decrypt(ct)
    print(pt)

r3, s4 = do_next(s2)
decrypt(r3 >> 8,cipher)

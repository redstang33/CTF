#!/usr/bin/env python3
import sys
import os
from Crypto.Cipher import AES
from base64 import b64encode
import pwn

cipher=""

#rem = pwn.process("./aesburgers.py")
rem = pwn.remote("46.101.107.117", 2207)


def getburger(patties, bun):
	rem.recvuntil("patties: ".encode())
	rem.sendline(str(patties).encode())
	rem.recvuntil("bun? ".encode())
	rem.sendline(bun.encode())
	rem.recvuntil("enjoy!\n".encode())
	cipher = rem.recvline().strip('\n'.encode())
	return cipher

ciphers={}
for i in range(1,25):
	cipher = getburger(i,"A"*16)
	ciphers[i] = cipher
	if cipher[:32] == cipher [-32:]:
		samecipher = i
print(samecipher, len(ciphers[samecipher]))		

# calculate length of the flag
flagsize=(len(ciphers[samecipher])//32*16-32)//samecipher
print("Flagsize is " + str(flagsize))

# based on that which cipher will be the one that ends in knowntext '}               ' (space is padding)
# we know the first 23 characters 'A'*16+'he2022{' patty*flag(35) + '}' + A'*16 + padding
# lets start in the back
# first get reference block with only one character unknown
# then brute force the unknown character

patties = {
	1: 11,
	2: 6,
	3: 1,
	4: 12,
	5: 7,
	6: 2,
	7: 13,
	8: 8,
	9: 3,
	10: 14,
	11: 9,
	12: 4,
	13: 15,
	14: 10,
	15: 5,
	16: 16
	}

position=0
flag = ("AAAAAAAAAAAAAA}A")
for i in range(1,17):
	for j in range(33,127): #only printable characters
		new = list(flag)
		new[15] = chr(j)
		flag=''.join(new)
		cipher = getburger(patties[i],flag)
		if cipher[:32] == cipher[-64:-32]:
			print("Position: "+str(position))
			position += 1
			print(flag)
			res = flag[1:16]+"A"
			flag=res

flag_1 = flag[::-1]
print(flag_1)

##first part done
# now get the rest of the flag

for i in range(1,17):
	for j in range(33,127): #only printable characters
		new = list(flag)
		new[15] = chr(j)
		flag=''.join(new)
		cipher = getburger(patties[i],flag)
		if cipher[:32] == cipher[-96:-64]:
			print("Position: "+str(position))
			position += 1
			print(flag)
			res = flag[1:16]+"A"
			flag=res

flag_2 = flag[::-1]
print(flag_2, flag_1)
# knownending=flagsize % 16 + samecipher
# print(knownending)
#!/usr/bin/env python3

import string

key="ACCEEBBDDFACCEBABAAAACCEEBBD"


cipher="augAlmepdpeuvlisvohxhqjxlfhr"


universe = [c for c in (chr(i) for i in range(32,127))]

uni_len = len(universe)
def vigenere(
        text: str, 
        key: str, 
        alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        encrypt=True
):

    result = ''

    for i in range(len(text)):
        letter_n = alphabet.index(text[i])
        key_n = alphabet.index(key[i % len(key)])

        if encrypt:
            value = (letter_n + key_n) % len(alphabet)
        else:
            value = (letter_n - key_n) % len(alphabet)

        result += alphabet[value]

    return result


def vigenere_encrypt(text, key):
    return vigenere(text=text, key=key, encrypt=True)


def vigenere_decrypt(text, key):
    return vigenere(text=text, key=key, encrypt=False)

def mixit(text):
	key = "GHBCANOPQRSTUVWXYZ12DEFIJKLM"
	nt = []
	for i in (string.ascii_uppercase+"12"):
		pos=key.find(i)
		nt.append(text[pos])
	nt = ''.join(nt)
	return(nt)


print(vigenere_decrypt(cipher, key))
print(mixit(vigenere_decrypt(cipher, key)))



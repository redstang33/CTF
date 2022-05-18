#!/usr/bin/env bash

for i in `cat /usr/share/wordlists/rockyou.txt`
do
	openssl aes-128-ecb -d -k $i -in secret.txt.enc | head -c 20
done
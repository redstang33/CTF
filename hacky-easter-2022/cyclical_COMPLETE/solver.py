#!/usr/bin/env python3

string = "abcdefghijklmnopqrstuvwxyz1234567890_{}"

numbers = [7,4,27,35,27,27,37,18604515501954,9089503077614,34052138441993,21227909669131,39663104618160,16103958750284,16456688276676,15426709948652,35366249530142,30753312664451,34621244773091,16094279020284,25308844326686,10237817005295,16074542603063,13960368551308,20563985455787,25423361916669,36367841662112]

i = 0
while i < 26:
    print(string[numbers[i]%39],end='')
    i+=1

print("\n")

# -*- coding: utf-8 -*-
import random
import platform
import string

def scan(i):
    stored = []
    for d in i:
        stored.append(d)
    return stored

def merge(i):
    return ''.join(i)

def encode(i):
    charmap = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    stored = reversed(i)
    stored = scan(stored)
    stored = ''.join(format(ord(x), random.choice(['1', '0'])) for x in stored)
    stored = scan(stored)
    stored = [x.replace('1', random.choice(charmap)) for x in stored]
    stored = [x.replace('2', random.choice(charmap)) for x in stored]
    stored = [x.replace('3', random.choice(charmap)) for x in stored]
    stored = [x.replace('4', random.choice(charmap)) for x in stored]
    stored = [x.replace('5', random.choice(charmap)) for x in stored]
    stored = [x.replace('6', random.choice(charmap)) for x in stored]
    stored = [x.replace('7', random.choice(charmap)) for x in stored]
    stored = [x.replace('8', random.choice(charmap)) for x in stored]
    stored = [x.replace('9', random.choice(charmap)) for x in stored]
    stored = [x.replace('0', '') for x in stored]
    stored = merge(stored)
    return(stored)
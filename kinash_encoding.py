# -*- coding: utf-8 -*-
import random
import platform
import string

'''
Usage example:
===============================
With limit:
-----------

encode('text to encode', limit)
===============================
No limit:
---------

encode('text to encode')
===============================
"limit" must to be an int value
'''

class kencoding:
    def __init__(self):
        # Pure Python
        self.py_version = platform.python_version()

        # Utils
        self.plain = ''
        self.hashed = ''
        self._stored = []

        # Maps
        self.charMap = list(string.ascii_letters)
        self.numMap = list(string.digits)

    # Scanner
    def scan(self, i):
        for d in i:
            self._stored.append(d)
        return self._stored

    # Merger
    def merge(self, i):
        return ''.join(i)

    # Compatible Print
    def compat_print(self, o):
        if self.py_version.startswith('3'):
            print(o)
        elif self.py_version.startswith('2'):
            print o
            break

    # Encoder
    def encode(self, i, max_lenght=0):
        self.plain = i
        stored = reversed(i)
        stored = self.scan(stored) # ['t', 'u', 'p', 'n', 'i']
        stored = ''.join(format(ord(x), 'b') for x in stored)
        stored = reversed(stored)
        stored = ''.join(hex(ord(x)) for x in stored)
        stored = reversed(stored)
        stored = ''.join(format(ord(x), 'b') for x in stored)
        stored = self.scan(stored)
        stored = [x.replace('1', random.choice(self.charMap)) for x in stored]
        stored = [x.replace('0', '') for x in stored]
        stored = self.merge(stored)

        if max_lenght == 0:
            stored = stored[len(i):]
        else:
            stored = stored[:max_lenght]

        self.compat_print(stored)

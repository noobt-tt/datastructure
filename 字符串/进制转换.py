# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:33:17 2019

@author: qwer_mt
"""

from string import digits, ascii_lowercase, ascii_uppercase
Alphabat = digits + ascii_lowercase + ascii_uppercase

def ten2any(n, b=62):
    assert b <= 62
    res = ''
    while n > 0:
        n, index = divmod(n, b)
        res = Alphabat[index] + res
        
    return res

def any2ten(s, b=62):
    n = 0
    for i, j in enumerate(reversed(s)):
        index = Alphabat.index(j)
        n += index * pow(b, i)
    return n

a = ten2any(8, 2)  #1000
b = ten2any(19,16)  #13
c = any2ten('a1',32)  #352  记得是字符串
print(a,b,c)
    

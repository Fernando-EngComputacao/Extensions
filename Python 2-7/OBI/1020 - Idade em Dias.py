# -*- coding: utf-8 -*-

x = input()

a = 0
m = 0
d = 0

while x != 0:
    if x >= 365:
        a += 1
        x -= 365
    elif x >= 30:
        m += 1
        x -= 30
    elif x < 30:
        d = x
        x = 0
        
print a,"ano(s)"
print m,"mes(es)"
print d,'dia(s)'

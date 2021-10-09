# -*- coding: utf-8 -*-

t = [int(o) for o in raw_input().split()]
a = t[0]
b = t[1]

while t[0] != 0 and t[1] != 0:
    s = a * b
    print s
    t = [int(o) for o in raw_input().split()]
    a = t[0]
    b = t[1]

# -*- coding: utf-8 -*-

a,b,c = raw_input().split()

a = int(a)
b = int(b)
c = int(c)

if a > b and a > c:
    print a,"eh o maior"
elif b > a and b > c:
    print b,'eh o maior'
else:
    print c,"eh o maior"

# -*- coding: utf-8 -*-
a,b,c = raw_input().split()

a = int(a)
b = int(b)
c = int(c)

ac = a
bc = a
cc = a

if b > a and b > c:
    cc = b
elif c > a and c > b:
    cc = c

if b < a and b < c:
    ac = b
elif c < a and c < b:
    ac = c

if b != ac and b != cc:
    bc = b
elif c != ac and c != cc:
    bc = c

print ac
print bc
print cc
print ""
print a
print b
print c

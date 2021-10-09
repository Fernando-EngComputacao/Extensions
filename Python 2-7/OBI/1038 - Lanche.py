# -*- coding: utf-8 -*-

a, b = raw_input().split()
a = int(a)
b = int(b)

if a == 1:
    t = (4 * b)
if a == 2:
    t = (4.5 * b)
if a == 3:
    t = (5 * b)
if a == 4:
    t = (2 * b)
if a == 5:
    t = (1.5 * b)
    
print "Total: R$ %.2lf" % (t)

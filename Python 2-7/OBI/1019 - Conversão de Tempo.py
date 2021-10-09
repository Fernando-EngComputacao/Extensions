# -*- coding: utf-8 -*-

z = input()

m = 0
s = 0
h = 0
while z != 0:
    if z >= 60:
        z -= 60
        m += 1
    elif z < 60:
        s += z
        z = 0
        
    if m >= 60:
        m -= 60
        h += 1
        
print "%s:%s:%s" % (h,m,s)

# -*- coding: utf-8 -*-
a,b,c,d = raw_input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if ((b > c and d > a) and ((c + d) > (a + b)) and (a % 2 == 0)):
    print "Valores aceitos"
else:
    print "Valores nao aceitos"

# -*- coding: utf-8 -*-

par = 0
i = 0
p = 0
n = 0

for e in range(0,5):
    u = input()
    if u > 0:
        p += 1
    elif u < 0 and u != 0:
        n += 1
        
    if u % 2 == 0:
        par += 1
    else:
        i += 1
        
print par,"valor(es) par(es)"
print i,"valor(es) impar(es)"
print p,"valor(es) positivo(s)"
print n,"valor(es) negativo(s)"


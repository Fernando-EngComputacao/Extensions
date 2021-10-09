# -*- coding: utf-8 -*-

a = input()

r = [int(u) for u in raw_input().split()]
m2 = 0
m3 = 0
m4 = 0
m5 = 0
for e in range(0, a):
    if r[e] % 2 == 0:
        m2 += 1
    if r[e] % 3 == 0:
        m3 += 1
    if r[e] % 4 == 0:
        m4 += 1
    if r[e] % 5 == 0:
        m5 += 1
print '%d Multiplo(s) de 2' % (m2)
print '%d Multiplo(s) de 3' % (m3)
print '%d Multiplo(s) de 4' % (m4)
print '%d Multiplo(s) de 5' % (m5)

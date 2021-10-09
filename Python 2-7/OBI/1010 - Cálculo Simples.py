# -*- coding: utf-8 -*-

A,B,C = raw_input().split()
A = int (A)
B = int (B)
C = float (C)

Aa,Bb,Cc = raw_input().split()
Aa = int (Aa)
Bb = int (Bb)
Cc = float (Cc)

A = (B * C) + (Bb * Cc)
print"VALOR A PAGAR: R$ %.2lf" % (A)

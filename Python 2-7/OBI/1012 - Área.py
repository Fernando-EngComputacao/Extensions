# -*- coding: utf-8 -*-

a,b,c = raw_input().split()

a = float(a)
b = float(b)
c = float(c)

t = (a * c)/2
bo = ((c * c)*3.14159)
tr = ((a + b)*c)/2
q = (b**2)
r = (a * b)
print "TRIANGULO: %.3lf" % (t)
print "CIRCULO: %.3f" % (bo)
print "TRAPEZIO: %.3lf" % (tr)
print "QUADRADO: %.3lf" % (q)
print "RETANGULO: %.3lf" % (r)

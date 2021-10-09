# -*- coding: utf-8 -*-

a,b,c = raw_input().split()

a = float(a)
b = float(b)
c = float(c)


delta = ((b**2)+((a*c)*(-4)))

if delta <= 0 or a == 0 or b == 0 or c == 0:
    print 'Impossivel calcular'
else:
    
    print "R1 = %.5lf" % (((-b) + (delta**0.5))/(2*a))
    print "R2 = %.5lf" %  (((-b) - (delta**0.5))/(2*a))

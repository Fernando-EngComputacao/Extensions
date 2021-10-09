# -*- coding: utf-8 -*-

z = input()

cem = 0
cin = 0
v = 0
d = 0
c = 0
do = 0
u = 0
print z
while z >= 100 or z >= 50 or z >= 20 or z >= 10 or z >= 5 or z >= 2 or z >= 1:
    if z >= 100:
        cem += 1
        z -= 100
        
    elif z >= 50:
        cin += 1
        z -= 50
        
    elif z >= 20:
        v += 1
        z -= 20
        
    elif z >= 10:
        d += 1
        z -= 10
        
    elif z >= 5:
        c += 1
        z -= 5

    elif z >= 2:
        do += 1
        z -= 2
        
    elif z >= 1:
        u += 1
        z -= 1
        

print cem,"nota(s) de R$ 100,00"
print cin,"nota(s) de R$ 50,00"
print v,"nota(s) de R$ 20,00"
print d,"nota(s) de R$ 10,00"
print c,"nota(s) de R$ 5,00"
print do,"nota(s) de R$ 2,00"
print u,"nota(s) de R$ 1,00"

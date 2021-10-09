# -*- coding: utf-8 -*-

num = input()
n100 = num // 100
num =  num - (n100*100)
n50 = num // 50
num = num - (n50*50)
n20 = num // 20
num = num - (n20*20)
n10 = num // 10
num = num - (n10*10)
n5 = num // 5
num = num - (n5 *5)
n2 = num // 2
num = num - (n2 *2)
m1 = num // 1
num = num - (m1 * 1)
m2 = num // 0.50
num = num - (m2 * 0.50)
m3 = num // 0.25
num = num - (m3 * 0.25)
m4 = num // 0.10
num = num - (m4 * 0.10)
m5 = num // 0.05
num = num - (m5 * 0.05)
m6 = num *100
print "NOTAS:"
print "%d nota(s) de R$ 100.00" %n100
print "%d nota(s) de R$ 50.00" %n50
print "%d nota(s) de R$ 20.00" %n20
print "%d nota(s) de R$ 10.00" %n10
print "%d nota(s) de R$ 5.00" %n5
print "%d nota(s) de R$ 2.00" %n2
print"MOEDAS:"
print "%d moeda(s) de R$ 1.00" %m1
print "%d moeda(s) de R$ 0.50" %m2
print "%d moeda(s) de R$ 0.25" %m3
print "%d moeda(s) de R$ 0.10" %m4
print "%d moeda(s) de R$ 0.05" %m5
print "%.0lf moeda(s) de R$ 0.01" %m6

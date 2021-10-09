# -*- coding: utf-8 -*-

nota1, nota2, nota3, nota4 = raw_input().split()

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

ponderada = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + (nota4)) / (10.0)
r = "Media: %.1lf" % (ponderada)
if ponderada >= 7.0:
    print r
    print "Aluno aprovado."

elif ponderada < 5.0:
    print r
    print "Aluno reprovado."

else:
    notaExame = input()
    print r
    print "Aluno em exame."
    print "Nota do exame: %.1lf" % (notaExame)
    notaFinal = ((ponderada + notaExame)/2.0)
    if notaFinal >= 5.0:
        print "Aluno aprovado."
    else:
        print "Aluno reprovado."
    print "Media final: %.1lf" % (notaFinal)

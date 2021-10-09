# -*- coding: utf-8 -*-

aux = 0
text = ""
vetor = []
valor  = [int(x) for x in raw_input().split()]

for a in range(1, int(valor[1]) + 1):
    vetor.append(a)

for t in range(0, len(vetor)):
    if aux != (int(valor[0]) + 1):
        if text == "":
            text += "%s" % (vetor[t])
        else:
            text += " %s" % (vetor[t])
        aux += 1
        if aux == (valor[0]):
            print "%s" % (text)
            text = ""
            aux = 0

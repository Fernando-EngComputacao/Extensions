A = []
for a in range(0,100):
    v = input()
    A.append(v)
    if v <= 10:
        print "A[%.lf] = %.1lf" % (a,v)

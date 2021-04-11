from time import time
from fractions import Fraction
start = time()
for n in range(10, 99):
    setn = set(str(n))
    if str(n).count("0") == 0 and str(n)[0] != str(n)[1]:
        for d in range(n + 1, 100):
            f = False
            if str(d).count("0") == 0 and str(d)[0] != str(d)[1]:
                setd = set(str(d))
                nn, nd = (setn - setd), (setd - setn)
                if len(nn) == len(nd) == 1:
                    nn = int(list(nn)[0])
                    nd = int(list(nd)[0])
                    f = True
                if f == True:
                    if Fraction(n, d) == Fraction(nn, nd):
                        print (n, d)
print (time() - start)

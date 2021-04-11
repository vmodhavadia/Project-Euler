from math import factorial
from time import time

#more efficient, checks up until certain value of nCr, then uses the symmetry
#of Pascal's Triangle to speed things up ~ 15ms

start = time()
count = 0
for n in range(23, 101):
    for r in range(3, n):
        if (factorial(n) / (factorial(r) * factorial(n - r))) > 1000000:
            count += ((n + 1) / 2) - r
            break
                

print (count * 2)
print (time() - start)
    

#less efficient, checks unnecessary values of nCr ~ 60ms

"""start = time()
count = 0
for n in range(23, 101):
    for r in range(0, n + 1):
        if (factorial(n) / (factorial(r) * factorial(n - r))) > 1000000:
            count += 1
                

print (count)
print (time() - start)"""

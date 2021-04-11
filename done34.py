from math import factorial
from time import time
s = time()
total = 0
for a in range(10, 100):
    A = str(a)
    if factorial(int(A[0])) + factorial(int(A[1])) == a:
        total += a
for b in range(100, 1000):
    B = str(b)
    if factorial(int(B[0])) + factorial(int(B[1])) + factorial(int(B[2])) == b:
        total += b
for c in range(1000, 10000):
    C = str(c)
    if factorial(int(C[0])) + factorial(int(C[1])) + factorial(int(C[2])) + factorial(int(C[3])) == c:
        total += c
for d in range(10000, 100000):
    D = str(d)
    if factorial(int(D[0])) + factorial(int(D[1])) + factorial(int(D[2])) + factorial(int(D[3])) + factorial(int(D[4])) == d:
        total += d
print (total)
print (time() - s)

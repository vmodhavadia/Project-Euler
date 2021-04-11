from time import time
start = time()
res = 10000
area = 0
for n in range(1, 2000):
    for m in range(1, 2000):
        if abs(2000000 - 0.25*m*n*(m+1)*(n+1)) < res:
            res = abs(2000000 - 0.25*m*n*(m+1)*(n+1))
            area = m*n
print (area, time() - start)

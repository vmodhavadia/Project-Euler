from time import time
s = time()
from math import factorial
lengths = [0 for i in range(0, 999999)]
count = 0
for i in range(1, 1000000):
    temp = [i]
    nlist = list(map(int, list(str(i))))
    while 6 == 6:
        n = 0
        for j in range(0, len(nlist)):
            n += factorial(nlist[j])
        temp.append(n)
        if temp.count(n) > 1 or (n < 999997 and lengths[n - 1] != 0):
            break
        nlist = list(map(int, list(str(n))))
    lengths[i - 1] = len(temp) - 1 + lengths[n - 1]
    if len(temp) - 1 + lengths[n - 1] == 60:
        count += 1
    #print (temp)

print (count)
print (time() - s)

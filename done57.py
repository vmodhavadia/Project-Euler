from time import time
start = time()
count = 0
n = 3
d = 2
for e in range(1, 1000):
    oldd = d
    d = oldd + n
    n = oldd + d
    if len(str(n)) > len(str(d)):
        count += 1

print (count)
print (time() - start)

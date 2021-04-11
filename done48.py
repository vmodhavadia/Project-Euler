from time import time
s = time()
counter = 0
for x in range(1, 1001):
    counter += x ** x
c = str(counter)
print (c[len(c) - 10::])
print (time() - s)

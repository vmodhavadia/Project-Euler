"""#brute force, slower and memory error
from time import time
start = time()
diags = []
width = 3
i = 1
increment = 2
numberofincrements = 0
while 6 != 7:
    if numberofincrements == 4:
        increment += 2
        width += 2
        numberofincrements = 0
    diags.append(i)
    i += increment
    numberofincrements += 1
    if width == 1003:
        break
print (sum(diags))
print (time() - start)"""

#more mathematical, faster
from time import time
start = time()
count = 0
for n in range(1, 501):  
    count += 4 * n * (4 * n + 1) # equal to((4 * n ** 2) + (4 * n)) + ((4 * n ** 2) - (2 * n)) + (4 * n ** 2) + ((4 * n ** 2) + (2 * n)) == (16 * n ** 2) + (4 * n)
print (count + (4 * n + 1))
print (time() - start)


from time import time
from itertools import permutations
s = time()
x = 125874
while 6 != 7:
    y = str(x)
    l = list(permutations(y, len(y)))
    if 1 == l.count(tuple(str(2 * x))) == l.count(tuple(str(3 * x))) == l.count(tuple(str(4 * x))) == l.count(tuple(str(5 * x))) == l.count(tuple(str(6 * x))):
        print (x)
        break
    elif int(y[1]) < 7:
        x += 1
    elif int(y[1]) == 7: 
        x += (int("1" + y) - x)

print (time() - s)   


    

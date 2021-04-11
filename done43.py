from itertools import permutations
from time import time
start = time()
pans = list(permutations("0123456789", 10))
z = []
for st in pans:
    s = "".join(st)
    if int(s[7:10]) % 17 == 0 == int(s[6:9]) % 13 == int(s[5:8]) % 11 == int(s[4:7]) % 7 and (s[5] == "5" or s[5] == "0") and int(s[2:5]) % 3 == int(s[3]) % 2 == 0:
        z.append(int(s))
        
print (sum(z))
print (time() - start)

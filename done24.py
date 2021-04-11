from itertools import permutations
from time import time
s = time()
print (''.join(list(permutations("0123456789"))[999999]))
print (time() - s)

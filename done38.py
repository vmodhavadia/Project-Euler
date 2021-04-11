# example shows first digit is 9 so number must start with 9
# if starting with 2 digit number, lengths are 2,3,3 which cannot give 9 digits
# if starting with 3 digit number, lengths are 3,4 which cannot give 9 digits
# if starting with 4 digit number, lengths are 4,5 which do give 9 digits
from time import time
start = time()
for n in range(9498, 9122, -1):
    if len(set(str(n) + str(n * 2))) == 9:
        print (str(n) + str(n * 2))
        break
print (time() - start)


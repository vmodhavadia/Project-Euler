from time import time
total = 0
s = time()
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
products = []
for z in range(1234, 98765):
    for x in range(2, 100):
        y = z / x
        i = []
        if y - int(y) == 0:
            i = list(str(int(y))+str(x)+str(z))
        if sorted(i) == nums:
            total += z
            break
print (total)
print (time() - s)

from time import time

s = time()

j = ""
for i in range(1, 185300):
    j += str(i)
    

print (int(j[0]) * int(j[9]) * int(j[99]) * int(j[999]) * int(j[9999]) * int(j[99999]) * int(j[999999]))
print (time() - s)

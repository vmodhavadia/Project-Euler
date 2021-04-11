from time import time
start = time()
count = 0
for i in range(10, 10000):
    j = i
    lychrel = True
    for iterations in range(50):
        j += int(str(j)[::-1])
        js = str(j)
        if js == js[::-1]:
            lychrel = False
            break
    if lychrel == True:
        count += 1

print (count)
print (time() - start)
"""even = "1234567887654321"
print (even[0:int(len(even)/2)], "start bit")
print (even[int(len(even)):int(len(even)/2-1):-1], "end bit")  

odd = "642353246"
print (odd[0:int(len(odd)/2)], "start bit")
print (odd[int(len(odd)):int(len(odd)/2):-1], "end bit")"""

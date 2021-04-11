from string import ascii_uppercase
from time import time
start = time()
count = 0
ts = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171]
a = list(ascii_uppercase)
f = open("42text.txt", "r")
l = f.read().split("\"")
for w in l:
    if w == "," or "":
        l.remove(w)
for x in l:
    t = 0
    y = list(x)
    for letter in y:
        t += (a.index(letter) + 1)
    if ts.count(t) == 1:
        count += 1
        
print (count)
print (time() - start)



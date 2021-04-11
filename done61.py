t, s, p, h, hep, o = [], [], [], [], [], []
for n in range(45, 141):
    if int(0.5*n*(n+1)) % 100 > 9:
        t.append(int(0.5*n*(n+1))) #end with 5, 0, 1, 8, 6, 3
for n in range(32, 100):
    if (n*n) % 100 > 9:
        s.append(n*n) #end with 1, 4, 9, 6, 5, 0
for n in range(26, 82):
    if (int(0.5*n*(3*n-1))) % 100 > 9:
        p.append(int(0.5*n*(3*n-1))) #end with 1, 0, 2, 7, 5, 6
for n in range(23, 71):
    if (n*(2*n-1)) % 100 > 9:
        h.append(n*(2*n-1)) #end with 5, 0, 1, 8, 6, 3
for n in range(21, 64):
    if (int(0.5*n*(5*n-3))) % 100 > 9:
        hep.append(int(0.5*n*(5*n-3))) #nothing (obviously) special about endings
for n in range(19, 59):
    if (n*(3*n-2)) % 100 > 9:
        o.append(n*(3*n-2)) #end with 5, 0, 1, 8, 6, 3

todelete = []
parent = t + s + p + h + hep + o
for i in parent:
    start = int(str(i)[0:2])
    f = False
    for j in parent:
        if j % 100 == start:
            f = True
            break
    if f == False:
        todelete.append(i)

print (todelete)
        


"""print (t)
print (s)
print (p)
print (h)
print (hep)
print (o)"""


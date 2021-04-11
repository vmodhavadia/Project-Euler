l = []
def thef(a):
    for b in range(2, 101):
        l.append(a ** b)

for a in range(2, 101):
    thef(a)

print (len(l))

newl = []
for term in l:
    if (newl.count(term) == 0):
        newl.append(term)

print (len(newl))
        
        

    

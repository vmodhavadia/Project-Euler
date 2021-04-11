from time import time
s = time()
f = False
x = []
pentagonals = [(n * (3 * n - 1) * 0.5) for n in range(990, 9999)]
for p in pentagonals:
    for P in pentagonals:
        if pentagonals.count(p + P) == 1:
            if pentagonals.count(abs(p - P)) == 1:
                x.append(p)
                x.append(P)
                f = True
                break
    if f == True:
        break
    
        
                
print (x)
print (max(x) - min(x))
print (time() - s)


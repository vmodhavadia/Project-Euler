from time import time
start = time()
def fun(i):
    z = 0
    ilist = list(map(int, list(str(i))))
    for m in ilist:
        z += m ** 2
    return z - 1

count = 0
nums = list(map(int, range(1, 10000000)))
g = [[] for i in range(0, 567)]
for i in nums:
    #g[(sum(list(map(int, list(str(i)))))) - 1].append(i)
    g[fun(i)].append(i)

for sub in g:
    if len(sub) != 0:
        flag = False
        n = sub[0]
        nlist = list(map(int, list(str(n))))
        while 6 == 6:
            n = 0
            for j in nlist:
                n += j ** 2
            if n == 89:
                flag = True
                break
            elif n == 1:
                break
            nlist = list(map(int, list(str(n))))
        if flag == True:
            count += len(sub)

print (count)
print (time() - start)
            
            
    

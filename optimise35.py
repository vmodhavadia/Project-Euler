from time import time
start = time()
def get_primes(n):
    m = n+1
    numbers = [True for i in range(m)]
    for i in range(2, int((n ** 0.5))):
        if numbers[i]:
          for j in range(i*i, m, i):
            numbers[j] = False
    primes = []
    for i in range(2, m):
        si = str(i)
        if numbers[i] and si.count("0") == si.count("2") == si.count("4") == 0 == si.count("6") == si.count("8") == si.count("5"):
          primes.append(i)
    return primes


primes = get_primes(1000000)
primess = get_primes(10000000)

count = 0
for p in primes:
    j = p
    rots = 0
    f = True
    while rots < len(str(j)) - 1:
        P = list(str(j))
        P.append(P[0])
        P.remove(P[0])
        x = int("".join(P))
        if primess.count(x) == 1:
            rots += 1
            j = str(x)
        else:
            f = False
            break
    if f == True:
        count += 1
                
print (count + 2)
print (time() - start)

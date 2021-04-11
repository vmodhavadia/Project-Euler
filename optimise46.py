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
        if numbers[i]:
          primes.append(i)
    return primes


primes = get_primes(200000)
primes.remove(2)
squares = [i ** 2 for i in range(450)]
nums = list(map(int, range(1, 200000, 2)))
nums.remove(1)
for p in primes:
    nums.remove(p)

for n in nums:
    f = False
    for s in squares:
        if 2 * s < n + 1:
            if primes.count(n - 2 * s) == 1:
                f = True
                break
    if f == False:
        print (n)
        break

print (time() - start)  
        


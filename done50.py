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


primes = get_primes(1000000)

total = 0
for n in range(3, 546):
    total += primes[n]
    if total > 1000000:
        break
print (total, primes.count(total) == 1)
    

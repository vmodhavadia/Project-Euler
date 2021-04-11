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


counts = []
check = get_primes(100000)
primes = get_primes(1000)
primes.reverse()
for b in primes:
    for a in range(-1001, 1001, 2):
        n = 0
        count = 0
        while check.count((n**2) + (a * n) + b) == 1:
            n += 1
            count += 1
        counts.append(count)
        if counts[len(counts) - 1] == max(counts):
            print (a, b)


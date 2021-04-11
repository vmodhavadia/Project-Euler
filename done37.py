"""def get_primes(n):
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
dick = get_primes(1000000)
for a in primes:
    A = str(a)
    b = len(A) - 1
    if A[0] == "4" or A[0] == "6" or A[0] == "8" or A[0] == "9" or A[b] == "0" or A[b] == "4" or A[b] == "6" or A[b] == "8":
        primes.remove(a)
primes.remove(2)
primes.remove(3)
primes.remove(5)
primes.remove(7)


total = 0
count = 0
for p in primes:
    if count == 11:
        break
    x = list(str(p))
    y = list(str(p))
    y.reverse()
    f = True
    while len(x) > 1:
        x.remove(x[0])
        y.remove(y[0])
        if dick.count(int("".join(x))) == 0 or dick.count(int("".join(y)[::-1])) == 0:
            f = False
            break
    if f == True:
        print (p)
        total += p
        count += 1

print ("total is %s" % (total))"""

#2 digit truncatable primes are 23, 37, 53, 73
#only '3' and '7' can be appended to them as otherwise they are not prime when truncated from left
#only '2', '3', '5', and '7' can be prepended to them (2 and 5 only if they are the last digits to be prepended)




    

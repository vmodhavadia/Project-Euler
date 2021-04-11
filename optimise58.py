from time import time
start = time()
def check(x):
    f = True
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            f = False
            break
    return f


p = 0
n = 1
while 6 == 6:
    x = (2*n)*(2*n-1) + 1
    if check(x) == True:
        p += 1
    x = 4 * n**2 + 1
    if check(x) == True:
        p += 1
    x = (2*n)*(2*n+1) + 1
    if check(x) == True:
        p += 1
    if p / (4 * n + 1) < 0.1:
        break
    n += 1
    
print ((n * 2) + 1)
print (time() - start)
# try checking if divisible by just primes instead of all numbers in check


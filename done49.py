from itertools import permutations
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

primes = get_primes(10000) #generates list of primes up to 10000

def diff(Perms):
    f = False
    for x in Perms:
        y = Perms.index(x) + 1 #sets y to the index of the next permutation after x
        while y < len(Perms):
            if Perms.count(Perms[y] + (Perms[y] - x)) >= 1 and primes.count(x) == primes.count(Perms[y]) == primes.count(Perms[y] + (Perms[y] - x)) == 1 and x > 1000 and Perms[y] - x != 0: # if difference between 
                print (x, Perms[y], Perms[y] + (Perms[y] - x), ", difference is", Perms[y] - x)
                for p in Perms:
                    if numbers.count(p) != 0:
                        numbers.remove(p)
                f = True
                break
            y += 1
        if f == True:
            break

numbers = list(map(int, range(1000, 10000))) #creates list of numbers to iterate over

for n in numbers:
    ns = str(n)
    if ns.count("0") + ns.count("2") + ns.count("4") + ns.count("6") + ns.count("8") == 4 or (int(ns[0]) + int(ns[1]) + int(ns[2]) + int(ns[3])) % 3 == 0:
        numbers.remove(n) #removes a number if it is composed entirely of even digits or if the sum of its digits is divisible by 3, as in these cases it will not be prime

for n in numbers:
    perms = list(map(tuple, permutations(str(n)))) #create a list of tuples of the permutations of number n
    Perms = []
    for p in perms:
        Perms.append(int("".join(p))) #add the tuple converted to an integer to new list
    diff(sorted(Perms)) #go to function which checks if permutations can be part of a sequence
print (time() - start)

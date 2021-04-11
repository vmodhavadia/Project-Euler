count = 2
primes = [2]
while count < 17:
    for i in primes:
        flag = True
        if (count % i == 0):
            flag = False
            break
    if flag == True:
        primes.append(i)
    count += 1
print (sum(primes))
    

from math import *
theprime = 6
primecount = 1
prime = 2
while primecount < 10000:
    for divisor in range(2, ceil(sqrt(prime)) + 2):
        flag = True
        if prime % divisor == 0:
            flag = False
            break
    if flag == True:
        theprime = prime
        primecount += 1
    prime += 1
print (theprime)
    
        
            
    

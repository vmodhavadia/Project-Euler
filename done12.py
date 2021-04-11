from math import sqrt
t = 1
c = 2
divisors = []
while 3 != 4:
    for divisor in range(1, int(sqrt(t))):
        if t % divisor == 0:
            divisors.append(divisor)
    if len(divisors) <= 250:
        t, c = t+c, c+1
        divisors.clear()
    elif len(divisors) > 250:
        break

print (t)

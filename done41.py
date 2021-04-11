from math import sqrt
pandigitals = []
for n in range(7654321, 6000000, -2):
    lsn = list(str(n))
    lsn = list(map(int, lsn))
    if lsn[len(lsn) - 1] != 5 and sum(lsn) % 3 != 0 and lsn.count(1) == lsn.count(2) == lsn.count(3) == lsn.count(4) == lsn.count(5) == lsn.count(6) == lsn.count(7) == 1:
        pandigitals.append(n)
        

for pan in pandigitals:
    flag = True
    for divisor in range(7, int(sqrt(pan))):
        if pan % divisor == 0:
            flag = False
            break
    if flag == True:
        print (pan)
        break







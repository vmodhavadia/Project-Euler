from time import time
start = time()
from math import sqrt, asin, pi
n = 40
while 6 == 6:
    a = (1 / n**2) + 1
    b = (-2 / n) - 2
    Px = (-b - sqrt(b**2 - (4 * a))) / (2 * a)
    Py = Px / n
    Qx = 1 + ((Px-1)/(1-Py))
    QO = sqrt((1-Qx)**2 + 1)
    theta = asin((1 - Qx)/QO)
    A = (0.5 * (1 - Qx)) - (0.5 * theta) + (0.5 * Px * Py)
    if (A / (1 - pi / 4)) < 0.001:
        break
    n += 1
print (n)
print (time() - start)

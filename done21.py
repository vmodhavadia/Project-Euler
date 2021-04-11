import time
start = time.time()
c = []

def amic(n):
    divisorsns = [m for m in range(1, int(n ** 0.5 + 1)) if n % m == 0]
    divisorsne = [n/a for a in divisorsns if a ** 2 != n and a != 1]
    x = sum(divisorsns + divisorsne)
    divisorsxs = [y for y in range(1, int(n ** 0.5 + 1)) if x % y == 0]
    divisorsxe = [x/b for b in divisorsxs if b ** 2 != x and b != 1]
    if sum(divisorsxs + divisorsxe) == n and x != n:
        c.append(x + n)
        
for n in range(220, 10000):
    amic(n)

print (sum(c) / 2)
print (time.time() - start)

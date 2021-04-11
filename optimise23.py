from time import time
start = time()
abundants = []
for n in range(12, 28124):
    smalldivisors = [sd for sd in range(1, int(n ** 0.5) + 1) if n % sd == 0]
    bigdivisors = [n / sd for sd in smalldivisors]
    bigdivisors.remove(n)
    if (n ** 0.5) % 1 == 0:
        bigdivisors.remove(n ** 0.5)
    if (sum(smalldivisors) + sum(bigdivisors)) > n:
        abundants.append(n)
print (time() - start)

canbewrittenassum = []
for a in abundants:
    for A in abundants:
        if a + A < 28124:
            canbewrittenassum.append(a + A)
        else:
            break

print (time() - start)

canbetwo = set(canbewrittenassum)
nums = set(map(int, range(1, 28124)))
tosum = list(nums - canbetwo)
print (sum(tosum))
print (time() - start)

        
            

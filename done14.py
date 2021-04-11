from time import time
s = time()
c = []
for j in range(1, 1000000):
    counter = 0
    while j != 1:
        if j <= len(c): # checks if j is in the list so instead of making a new chain
            counter += c[int(j - 1)] # it just adds onto the length of the other one
            break
        if j % 2 == 0:
            j = j / 2
        else:
            j = (3 * j) + 1
        counter += 1
    c.append(counter)
print (c.index(max(c)) + 1)
print (time() - s)


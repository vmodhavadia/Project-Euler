from time import time
start = time()
count = 0
f = open('102text.txt', 'r')
for line in f:
    xs, ys = [], []
    L = list(map(int, line.split(',')))
    if L[2] == L[4] or L[0] == L[4] or L[0] == L[2] or L[1] == L[3] or L[3] == L[5]:
        pass
    else:
        m12 = (L[3] - L[1]) / (L[2] - L[0])
        if L[2] <= ((m12 * L[2] - L[3]) / m12) <= L[0] or L[2] >= ((m12 * L[2] - L[3]) / m12) >= L[0]:  
            xs.append((m12 * L[2] - L[3]) / m12)

        if L[3] <= (L[3] - m12 * L[2]) <= L[1] or L[3] >= (L[3] - m12 * L[2]) >= L[1]:
            ys.append(L[3] - m12 * L[2])


        m13 = (L[5] - L[1]) / (L[4] - L[0])
        if L[4] <= ((m13 * L[4] - L[5]) / m13) <= L[0] or L[4] >= ((m13 * L[4] - L[5]) / m13) >= L[0]:  
            xs.append((m13 * L[4] - L[5]) / m13)

        if L[5] <= (L[5] - m13 * L[4]) <= L[1] or L[5] >= (L[5] - m13 * L[4]) >= L[1]:
            ys.append(L[5] - m13 * L[4])


        m23 = (L[5] - L[3]) / (L[4] - L[2])
        if L[2] <= ((m23 * L[4] - L[5]) / m23) <= L[4] or L[2] >= ((m23 * L[4] - L[5]) / m23) >= L[4]:  
            xs.append((m23 * L[4] - L[5]) / m23)

        if L[5] <= (L[5] - m23 * L[4]) <= L[3] or L[5] >= (L[5] - m23 * L[4]) >= L[3]:
            ys.append(L[5] - m23 * L[4])

        if len(xs) != 0 and len(ys) != 0:
            if xs[0] * xs[1] < 0 and ys[0] * ys[1] < 0:
                count += 1

print (count)
print (time() - start)
    

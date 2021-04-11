N = 40 #number of nodes
f = open('107text.txt', 'r')
networksum = 0
m = []
for line in f:
    line = line.split(',')
    for i in range(0,40):
        if line[i].count('-') == line[i].count('n') == 0:
            line[i] = int(line[i])
            networksum += line[i]
        else:
            line[i] = 1000 #change 1000 to a number greater than the maximum value in m
    m.append(line)

mstsum = 0
active = []
a = 0
for passes in range(0, N-1):
    for i in range(0, N):
        m[i][a] = 1000 #change 1000 to a number greater than the maximum value in m
    if active.count(a) == 0:
        active.append(a)
    minvals = [1000 for j in range(0, N)] #change 1000 to a number greater than the maximum value in m
    for A in active:
        minvals[A] = min(m[A])
    mstsum += min(minvals)
    a = m[minvals.index(min(minvals))].index(min(m[minvals.index(min(minvals))]))
    
print ("saving of " + str(0.5 * networksum - mstsum))
        
    

        
            





    


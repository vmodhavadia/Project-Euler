ex = 3 #number corresponding to n1, d1
n1, d1 = 8, 3
n2, d2 = 11, 4
n3, d3 = 19, 7
while ex != 101:
    print (n1, n2, n3)
    n1, d1 = n2 + (ex + 1) * n3, d2 + (ex + 1) * d3
    n2, d2 = n3 + n1, d3 + d1
    n3, d3 = n1 + n2, d1 + d2
    ex += 2



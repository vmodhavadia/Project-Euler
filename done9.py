for a in range(1, 500):
    for b in range(1, 500):
        for c in range(1, 500):
            if ((a ** 2 + b ** 2 == c ** 2) and (a + b + c == 1000)):
                print (a,b,c, a * b * c)


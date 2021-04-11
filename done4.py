gays = []
for i in range(100, 999):
    for j in range(100, 999):
        prod = str(i * j)
        if (prod == prod[::-1]):
            print (prod)
        

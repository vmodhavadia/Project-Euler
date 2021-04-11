f = open("79text.txt", "r")
c = 0
for l in f:
    if l[1] == "9":
        c += 1
print (c)
    

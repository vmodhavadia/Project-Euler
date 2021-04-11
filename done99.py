from math import *
finals = [1]
f = open("99text.txt", "r")
linenumber = 0
for l in f:
    x = l.split(",")
    x[1].split("\n")
    logged = int(x[1]) * log10(int(x[0]))
    linenumber += 1
    if (logged > max(finals)):
        finals.clear()
        finals.append(logged)
        finals.append(linenumber)

print (finals)
    

    
    





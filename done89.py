savings = 0
numerals = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
dec = [1000, 500, 100, 50, 10, 5, 1]
f = open('89text.txt', 'r')
for l in f:
    k = list(reversed(list(l)[0:len(list(l))-1]))
    n = dec[numerals.index(k[0])]
    for i in range(1, len(k)):
        if numerals.index(k[i]) > numerals.index(k[i-1]):
            n -= dec[numerals.index(k[i])]
        else:
            n += dec[numerals.index(k[i])]
    nlist = list(map(int, list(str(n))))
    minlen = 0
    for i in range(0, len(nlist)):
        if nlist[i] == 1 or nlist[i] == 5:
            minlen += 1
        elif nlist[i] == 2 or nlist[i] == 6 or nlist[i] == 9:
            minlen += 2
        elif nlist[i] == 3 or nlist[i] == 7:
            minlen += 3
        elif nlist[i] == 8 or (nlist[i] == 4 and i == 0 and n >= 1000):
            minlen += 4
        elif nlist[i] == 0:
            minlen += 0
        elif nlist[i] == 4:
            minlen += 2
    savings += (len(k) - minlen)

print (savings)

#because last line has no new line character, discount it and check it manually

                     

    
            
        
    

# brute force
count = 0
for i in range(10, 10000000):
    if (str(i)[len(str(i))-1]) != '0':
        x = str(i + int(str(i)[::-1]))
        if x.count("0") == x.count("2") == x.count("4") == x.count("6") == x.count("8") == 0:
            count += 1

print (count)

"""# clever way for 3 digits: breaks ruined other one
from math import floor
evens = [0, 2, 4, 6, 8]
count = 0
for c in range(1, 10):
    for a in range(1, 10):
        if ((c+a)%10)%2 == 1:
            fca = floor((c+a)/10)
            for b in range(0, 10):
                if ((b+b+fca)%10)%2 == 1:
                    fbb = floor((b+b+fca)/10)
                    if (a+c+fbb)%2 != 0:
                        count += 1

print (count)"""

"""#now for 4 digits
from math import floor
evens = [0, 2, 4, 6, 8]
count = 0
for d in range(1, 10):
    for a in range(1, 10):
        if ((d+a)%10)%2 == 1:
            fda = floor((d+a)/10)
            for c in range(0, 10):
                for b in range(0, 10):
                    if ((c+b+fda)%10)%2 == 1:
                        fcb = floor((c+b+fda)/10)
                        fbc = floor((b+c+fcb)/10)
                        if ((b+c+fcb)%10)%2 == 1 and (a+d+fbc)%2 == 1:
                            count += 1

print (count)"""

        


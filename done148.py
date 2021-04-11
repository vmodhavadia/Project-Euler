myli = []
rows = 7
total = 28
for a in [56, 84, 112, 140, 168, 196]:
    total += a
    rows += 7
    for b in range(1, 8):
        total += a*b
        rows += 7
        for c in range(1, 8):
            total += a*b*c
            rows += 7
            for d in range(1, 8):
                total += a*b*c*d
                rows += 7
                for e in range(1, 8):
                    total += a*b*c*d*e
                    rows += 7
                    for f in range(1, 8):
                        total += a*b*c*d*e*f
                        rows += 7
                        for g in range(1, 8):
                            total += a*b*c*d*e*f*g
                            rows += 7
                            for h in range(1, 8):
                                total += a*b*c*d*e*f*g*h
                                rows += 7
                                for i in range(1, 8):
                                    total += a*b*c*d*e*f*g*h*i
                                    rows += 7
                                    myli.append(a*b*c*d*e*f*g*h*i)
                                    

#print (str(total) + " entries aren't divisible by 7")
#print (str(rows) + " rows so far")
flag = False
for j in myli:
    for m in range(1, 8):
        if rows == 999999994:
            flag = True
            break
        else:
            total += j*m
            rows += 7
    if flag == True:
        break

print ("so far " + str(total) + " entries")
print ("deal with " + str(j*m))

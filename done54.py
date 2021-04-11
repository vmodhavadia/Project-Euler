from statistics import mode
f = open("54text.txt", "r")
nums = '123456789'
count = 0
for line in f:
    one = ''.join(line[0:14].split())
    oneN, oneS = [], []
    for i in one:
        if nums.count(i) == 1: oneN.append(int(i))
        elif i == "T": oneN.append(10)
        elif i == "J": oneN.append(11)
        elif i == "Q": oneN.append(12)
        elif i == "K": oneN.append(13)
        elif i == "A": oneN.append(14)
        else: oneS.append(i)
    two = ''.join(line[15:29].split())
    twoN, twoS = [], []
    for i in two:
        if nums.count(i) == 1: twoN.append(int(i))
        elif i == "T": twoN.append(10)
        elif i == "J": twoN.append(11)
        elif i == "Q": twoN.append(12)
        elif i == "K": twoN.append(13)
        elif i == "A": twoN.append(14)
        else: twoS.append(i)
    onescore, twoscore = 0.0, 0.0
    if oneS.count(oneS[0]) == 5 and oneN.count(min(oneN)) == oneN.count(min(oneN)+1) == oneN.count(min(oneN)+2) == 1 == oneN.count(min(oneN)+3) == oneN.count(min(oneN)+4): onescore = 9
    elif oneN.count(min(oneN)) == 4 or oneN.count(max(oneN)) == 4: onescore = 8
    elif (oneN.count(min(oneN)) == 3 and oneN.count(max(oneN)) == 2) or (oneN.count(min(oneN)) == 2 and oneN.count(max(oneN)) == 3): onescore = 7
    elif oneS.count(oneS[0]) == 5: onescore = 6
    elif oneN.count(min(oneN)) == oneN.count(min(oneN)+1) == oneN.count(min(oneN)+2) == 1 == oneN.count(min(oneN)+3) == oneN.count(min(oneN)+4): onescore = 5
    elif oneN.count(oneN[0]) == 3 or oneN.count(oneN[1]) == 3 or oneN.count(oneN[2]) == 3: onescore = 4
    elif len(set(oneN)) == 3 and oneN.count(oneN[0]) != 3 and oneN.count(oneN[1]) != 3 and oneN.count(oneN[2]) != 3: onescore = 3
    elif len(set(oneN)) == 4: onescore = 2
    else: onescore = 1 - (1 / max(oneN))

    if twoS.count(twoS[0]) == 5 and twoN.count(min(twoN)) == twoN.count(min(twoN)+1) == twoN.count(min(twoN)+2) == 1 == twoN.count(min(twoN)+3) == twoN.count(min(twoN)+4): twoscore = 9
    elif twoN.count(min(twoN)) == 4 or twoN.count(max(twoN)) == 4: twoscore = 8
    elif (twoN.count(min(twoN)) == 3 and twoN.count(max(twoN)) == 2) or (twoN.count(min(twoN)) == 2 and twoN.count(max(twoN)) == 3): twoscore = 7
    elif twoS.count(twoS[0]) == 5: twoscore = 6
    elif twoN.count(min(twoN)) == twoN.count(min(twoN)+1) == twoN.count(min(twoN)+2) == 1 == twoN.count(min(twoN)+3) == twoN.count(min(twoN)+4): twoscore = 5
    elif twoN.count(twoN[0]) == 3 or twoN.count(twoN[1]) == 3 or twoN.count(twoN[2]) == 3: twoscore = 4
    elif len(set(twoN)) == 3 and twoN.count(twoN[0]) != 3 and twoN.count(twoN[1]) != 3 and twoN.count(twoN[2]) != 3: twoscore = 3
    elif len(set(twoN)) == 4: twoscore = 2
    else: twoscore = 1 - (1 / max(twoN))

    if onescore > twoscore: count += 1
    elif onescore == twoscore == 9 and min(oneN) > min(twoN): count += 1
    elif (onescore == twoscore == 8 or onescore == twoscore == 7) and mode(oneN) > mode(twoN): count += 1
    elif onescore == twoscore == 6 and ((sorted(oneN)[4] > sorted(twoN)[4]) or (sorted(oneN)[4] == sorted(twoN)[4] and sorted(oneN)[3] > sorted(twoN)[3])): count += 1
    elif onescore == twoscore == 5 and min(oneN) > min(twoN): count += 1
    elif onescore == twoscore == 4 and mode(oneN) > mode(twoN): count += 1
    elif onescore == twoscore == 3:
        for i in oneN:
            if oneN.count(i) == 1:
                oddone = oneN.pop(i)
                break
        for j in twoN:
            if twoN.count(j) == 1:
                oddtwo = twoN.pop(i)
                break
        if max(oneN) > max(twoN): count += 1
        elif max(oneN) == max(twoN) and min(oneN) > min(twoN): count += 1
        elif max(oneN) == max(twoN) and min(oneN) == min(twoN) and oddone > oddtwo: count += 1
    elif onescore == twoscore == 2 and mode(oneN) > mode(twoN): count += 1
print (count)

    



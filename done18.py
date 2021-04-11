t = \
"63 66 04 68 89 53 67 30 73 16 69 87 40 31 \n\
91 71 52 38 17 14 91 43 58 50 27 29 48 \n\
70 11 33 28 77 73 17 78 39 68 17 57 \n\
53 71 44 65 25 43 91 52 97 51 14 \n\
41 48 72 33 47 32 37 16 94 29 \n\
41 41 26 56 83 40 80 70 33 \n\
99 65 04 28 06 16 70 92 \n\
88 02 77 73 07 63 67 \n\
19 01 23 75 03 34 \n\
20 04 82 47 65 \n\
18 35 87 10 \n\
17 47 82 \n\
95 64 \n\
75 "
ttolist = []
listoflines = t.split("\n") #splits triangle into lines
for line in listoflines:
    line = line.split(" ")#splits line into numbers
    line.remove('') #removes space at end
    line = list(map(int, line)) #maps list of string to list of integer
    ttolist.append(line) #adds line of numbers to another list
start = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
for line in ttolist:
    i = 0
    while i < len(line):
        line[i] += max(start[i], start[i+1])
        i += 1
    start = line
print (line)
        


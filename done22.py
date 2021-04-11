import string
f = open("22text.txt", "r")
names = f.read()
listnames = names.split("\"")
for charcheck in listnames:
    if len(charcheck) <= 1:
        listnames.remove(charcheck)
listnames = sorted(listnames)
alphabet = list(string.ascii_uppercase)
thelist = []
for name in listnames:
    sliced = list(name)
    total = 0
    for letter in alphabet:
        if sliced.count(letter) > 0:
            total += ((alphabet.index(letter) + 1) * sliced.count(letter))
    thelist.append((listnames.index(name) + 1) * total)
    total = 0
print (sum(thelist))


            
        
    


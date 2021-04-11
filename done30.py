mylist = []
for i in range(1, 354294):
    s = list(str(i))
    total = 0
    for digit in s:
        digit = int(digit)
        total += digit ** 5
    if total == i and i != 1:
        mylist.append(i)
print (mylist, sum(mylist))
        
        
    

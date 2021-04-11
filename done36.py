palindromes = []
for i in range(1, 1000001):
    reverse10 = ((str(i))[::-1])
    reverse2 = ((str(bin(i)))[:1:-1])
    if reverse10 == str(i) and reverse2 == str(bin(i))[2::1]:
        palindromes.append(i)

print (sum(palindromes))







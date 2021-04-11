from decimal import Decimal, getcontext
getcontext().prec = 102
total = 475
nums = list(range(3, 100))
nums.remove(4)
nums.remove(9)
nums.remove(16)
nums.remove(25)
nums.remove(36)
nums.remove(49)
nums.remove(64)
nums.remove(81)

for n in nums:
    s = str(Decimal(n ** Decimal(0.5)))
    s = (s[0:len(s)-2] + s[0])[2::]
    total += sum(map(int, list(s)))

print (total)


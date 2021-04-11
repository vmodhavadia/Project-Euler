mylist = []
for a in range(1, 100):
   for b in range(1, 100):
      s = list(str(a ** b))
      digitalsum = 0
      for c in s:
         digitalsum += int(c)
      mylist.append(digitalsum)
      digitalsum -= digitalsum
print (max(mylist))


from time import time
s = time()
for i in range(1389026630, 1058921220, -10):
    x = str(i**2)
    if x[0]=="1" and x[2]=="2" and x[4]=="3" and x[6]=="4" and x[8]=="5" and x[10]=="6" and x[12]=="7" and x[14]=="8" and x[16]=="9" and x[18]=="0":
        print (i)
        break
print (time() - s)       
    


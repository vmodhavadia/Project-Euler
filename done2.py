#a = int(input("Enter how many values of the Fibonacci Sequence you would like ")) # asks for how many values user wants
b = 0 # initialises counter for while loop to 0
x, y = 0, 1 # first 2 terms of sequence
#print (0) # prints first term (0), which is otherwise ommitted
evens = []
while y <= 4000000:#a - 1:
    if (y % 2 == 0):
        evens.append(y)
    #print (y), # as long as b is in range of users desired number of values, print y
    x, y = y, x + y 
    #b += 1 # increments b by 1
print (sum(evens))


from random import randrange
x = (randrange(1, 10000))
y = (randrange(1, 10000))

if y > x:
    print ("The greater variable is y")
    print (f"The variable X is {x}")
    print (f"The variable Y is {y}")
if x > y:
    print ("The greater variable is x")
    print (f"The variable X is {x}")
    print (f"The variable Y is {y}")
print ("The range of the randomizer is from 1 to 10000")

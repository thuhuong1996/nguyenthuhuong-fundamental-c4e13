from random import randint
n =randint(1,100)
while True:
    i = int(input("Enter your answer"))
    if i == n:
        print ("your number is correct")
    elif i > n:
        print ("your number is too big")
    else:
        print(" your number is too small")

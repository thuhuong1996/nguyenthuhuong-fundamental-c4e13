listofnumber = [1, 2, 3, 4, 5, 1, 4]
yournumber= int(input("Enter your number:"))
count = 0
for number in listofnumber:
 if yournumber == number:
    count += 1
    print("your number appears in the list for:", count , "times")

 else:
    print("your number is not in the list")

print ("Welcome to our shop")
ouritems= ["T-shirt" , "Sweater"]
n = input("Enter new items")
ouritems.append(n)
print (*ouritems, sep = ',' )

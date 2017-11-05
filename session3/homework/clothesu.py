print("Welcome to our shop")
n = input ("Enter new items:")
i = int ( input (" Enter the position:"))
ouritems = ["T-shirt", "Jeans"]
ouritems.insert (i,n)
print (*ouritems, sep = ',')

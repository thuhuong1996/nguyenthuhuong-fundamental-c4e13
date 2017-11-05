print("Hello, my name is Hiep and here is my sheep sizes:")
size= [5,7,300,90,24,50,75]
n= max(size)
size.remove(n)
print ("Now my biggest sheep has the size", n, "let's shear it")
print ("After shearing, here is my flock",*size)

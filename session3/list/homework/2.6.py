print("Hello, my name is Hiep and here is my sheep sizes:")
size= [5,7,300,90,24,50,75]
n= max(size)
print ("Now my biggest sheep has the size", n, "let's shear it")
size.remove(n)
print ("After shearing, here is my flock",*size)
size= [50+5,50+7,50+90,50+24,50+50,75+50]
print ("One month has passed, now my flock is:", size)
m= max(size)
size.append(8)
print ("Now my biggest sheep has the size", m, "let's shear it")
size.remove(m)
print ("After shearing, here is my flock",*size)
print ("One month has passed, now my flock is:", size)
size= [100+5,100+7,100+24,100+50,100+75,50+8]
h= max(size)
size.append(8)
print ("Now my biggest sheep has the size", h, "let's shear it")
size.remove(h)
print ("After shearing, here is my flock",*size)
size= [150+5,150+7,150+8,100+8,150+24,150+50,50+8]
print ("One month has passed, now my flock is:", size)
a= sum(size)
print("My flock has size in total:", a)
b=a*2
print("I would get:", b, "$")

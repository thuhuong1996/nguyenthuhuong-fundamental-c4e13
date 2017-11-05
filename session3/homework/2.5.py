print("Hello, my name is Hiep and here is my sheep sizes:")
size= [5,7,300,90,24,50,75]
print ("One month has passed, now here my flock is:", *size)
size= [50+5,50+7,50+300,50+90,50+24,50+50,50+50]
m=max(size)
size.remove(m)
print ("Now my biggest sheep has the size", m , "let's shear it")
size.append(8)
print ("After shearing, here is my flock",*size)
print ("One month has passed, now my flock is:", *size)
size= [100+5,100+7,100+90,100+24,100+50,100+50,8+50]
n=max(size)
size.remove(n)
print ("Now my biggest sheep has the size", n , "let's shear it")
size.append(8)
print ("After shearing, here is my flock",*size)
print ("One month has passed, now my flock is:", *size)
size= [150+5,150+7,150+24,150+50,150+50, 8+100, 8+50]
h=max(size)
size.remove(h)
print ("Now my biggest sheep has the size", h , "let's shear it")
size.append(8)
print ("After shearing, here is my flock",*size)

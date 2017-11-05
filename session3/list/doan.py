menu = ["a", "b", "c", "d"]
print(menu)
n = input ("mon an ban khong thich nhat? ")
if n in menu:
 menu.remove(n)
 print(*menu, sep= ',' )
else:
 print (n, " khong co trong menu")

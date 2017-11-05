menu = [" com ", " thit"]
for i in range( len (menu)):
    print(i+1, menu[i])
n = input("mon an ban muon update?")
h = int(input (" vi tri ban muon update?"))
menu.insert(h, n)
# print (*menu)

for i in range( len (menu)):
    print(i+1, menu[i])

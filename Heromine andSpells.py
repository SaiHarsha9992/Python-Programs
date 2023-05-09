x = int(input())
y = int(input())
z = int(input())
if(x<y) and (x<z):
    print(y+z)
elif (y<x) and (y<z):
    print(x+z)
else:
    print(x+y)
a = int(input())
b = int(input())
c = int(input())
if (a > b) and (a > b) and (a > c):
   l = a
elif ( b > a) and (b > c) and ( c > a ):
   l = b
else:
   l = c

print(l)
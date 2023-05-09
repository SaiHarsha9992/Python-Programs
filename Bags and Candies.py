n = int(input())
k = int(input())
m = int(input())
y = n//(m*k)
if (n%(m*k)!=0):
    y+=1
print(y)

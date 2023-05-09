n = int(input())
k = int(input())
x= int(input())
y = int(input())
kt=k*x
b=x*(n-k)
a=y*(n-k)
if(a>b):
        t=kt+b
        print(t)
else:
        t=kt+a;
        print(t)

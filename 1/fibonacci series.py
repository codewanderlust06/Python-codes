a=0
b=1
c=0
n=int(input("Enter a Number of items = "))
print(a)
print(b)
for i in range(0,n-2):
    c=a+b
    print(c)
    a=b
    b=c

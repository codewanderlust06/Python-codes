n=int(input("Enter total no. of elements of list = "))
lst=[]
print("Enter",n,"elements of the list:")
for i in range(0,n):
    temp=int(input())
    lst.append(temp)
for x in lst:
    if x<5:
        print(x," ",end="")

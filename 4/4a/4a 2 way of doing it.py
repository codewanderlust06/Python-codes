n1=int(input("Enter a first list = "))
lst1=[]
for i in range(0,n1):
    temp=int(input())
    lst1.append(temp)
n2=int(input("Enter a second list = "))
lst2=[]
for i in range(0,n2):
    temp=int(input())
    lst2.append(temp)

for x in lst1:
    if x in lst2:
        print(True)
        break
else:
    print(False)

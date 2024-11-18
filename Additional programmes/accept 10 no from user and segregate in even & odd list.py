Elst=[]
Olst=[]
for i in range(10):
    n=int(input("Enter a No = "))
    if n%2==0:
        Elst.append(n)
    else:
        Olst.append(n)
    print("Even list is : ",Elst)
    print("Odd list is : ",Olst)

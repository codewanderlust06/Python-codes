Plst=[]
NPlst=[]
for i in range(10):
    n=int(input("Enter a No = "))
    if n%1==0:
        NPlst.append(n)
        f=1
        break
if f==0:
    Plst.append(n)
    print("Prime list is : ",Plst)
    print("Non Prime list is : ",NPlst)
    

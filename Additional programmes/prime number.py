n=int(input("Enter a Number = "))
f=0
for i in range(2,n):
    if (n%i)==0:
        print("Number is not Prime")
        f=1
        break
if(f==0):
        print("Number is Prime")

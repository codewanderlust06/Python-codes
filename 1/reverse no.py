def ReverseNo(n):
    p=0
    rem=0
    while(n>0):
        rem=n%10
        p=(p*10)+rem
        n=n//10
    return p
n1=int(input("Enter a Number = "))
rv_No=ReverseNo(n1)
print("Reverse of ",n1," is ", rv_No)



n1=int(input("Enter a number : "))
def armstrong(n):
    n_copy=n
    p=0
    rem=0
    while(n>0):
        rem=n%10
        p=p+rem*rem*rem
        n=n//10
    if(n_copy==p):
        print("Number is Armstrong")
    else:
        print("Number is not Armstrong")
armstrong(n1) #Function call

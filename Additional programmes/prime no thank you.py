def CheckPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
while(True):
    n=int(input("Enter a Number : "))
    if CheckPrime(n):
        print("Thank You")
        break

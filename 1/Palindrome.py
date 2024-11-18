def Palindrome(n):
    n_copy=n
    rem=0
    rev=0
    while (n>0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if(rev==n_copy):
        print(n_copy,'Number is a Palindrome')
    else:
            print(n_copy,'Number is not Palindrome')
Palindrome(1221)

n=int(input("Enter a number: "))
try:
    re=25/n
except(ValueError,ZeroDivisionError):
    print("Wrong value is inserted")
else:
    print("Result is: ",re)
finally:
    print("Clean-up is done")

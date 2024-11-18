class Numbers:
    MULTIPLIER=15.2

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self):
        return(self.x+self.y)

    def multiply(cls,a):
        return(a*cls.MULTIPLIER)

    def subtract(b,c):
        return(b-c)

    def value(self):
        return(self.x,self.y)

    def value(self,tup):
        self.x=tup[0]
        self.y=tup[1]

    def value(self):
        del self.x
        del self.y


n=Numbers(10,20)
print("Addition is: ",n.add())
print("Multiplication is: ",n.multiply(12))
print("Subtraction is: ",Numbers.subtract(32,16))

n.value=(30,40)
print("Value Set using setter")
print("Getter: ",n.value)
del n.value
print("Check: ",n.value)




        


        
    

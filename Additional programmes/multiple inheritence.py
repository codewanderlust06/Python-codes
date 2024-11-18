class st1:
    def num1(self):
        self.n1=7
        print("No.1",self.n1)
class st2:
    def num2(self):
        self.n2=2
        print("No.2",self.n2)

class st(st1,st2):
    def add(self):
        return self.n1+self.n2

s=st()
s.num1()
s.num2()
print(s.add())

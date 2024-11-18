class T:
    def show(self):
        print("Base class")
class S(T):
    def show1(Self):
        super().show()
        print("Derived class")

v=S()
v.show()

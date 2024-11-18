class student:
    def __init__(self,sno,sname,age,course):
        self.sno=sno
        self.sname=sname
        self.age=age
        self.course=course
    def displayStudentDetails(self):
        print("******Student Details******")
        print("Student No: ",self.sno)
        print("Student Name: ",self.sname)
        print("Student Age: ",self.age)
        print("Student Course: ",self.course)

print("Enter Details for Student 1: ")
sn1=int(input("Enter Sno: "))
name1=input("Enter Name: ")
age1=int(input("Enter Age: "))
course1=input("Enter Course: ")

s1=student(sn1,name1,age1,course1)

print("Enter Details for Student 2: ")
sn2=int(input("Enter Sno: "))
name2=input("Enter Name: ")
age2=int(input("Enter Age: "))
course2=input("Enter Course: ")

s2=student(sn2,name2,age2,course2)

s1.displayStudentDetails()
s2.displayStudentDetails()













 

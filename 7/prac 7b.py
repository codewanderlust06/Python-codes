class CompanyMember:
    def __init__(self,name,designation,age):
        self.name=name
        self.designation=designation
        self.age=age
    def DisplayCompanyStaff(self):
        print("Name: ",self.name)
        print("Designation: ",self.designation)
        print("Age: ",self.age)

class FactoryStaff(CompanyMember):
    def __init__(self,name,designation,age,overtime_allowance):
        CompanyMember.__init__(self,name,designation,age)
        self.overtime_allowance=overtime_allowance
    def DisplayFactoryStaff(self):
        print("Factory Staff Details: ")
        CompanyMember.DisplayCompanyStaff(self)
        print("OverTime Allowance: ",self.overtime_allowance)

class OfficeStaff(CompanyMember):
    def __init__(self,name,designation,age,travel_allowance):
        CompanyMember.__init__(self,name,designation,age)
        self.travel_allowance=travel_allowance
    def DisplayOfficeStaff(self):
        print("OfficeStaff Details: ")
        CompanyMember.DisplayCompanyStaff(self)
        print("Travel Allowance: ",self.travel_allowance)
        

f1=FactoryStaff("Allen","Sr.Engg",34,1500)
f2=OfficeStaff("Smith","HR Admin",34,1200)


f1.DisplayFactoryStaff()
f2.DisplayOfficeStaff()







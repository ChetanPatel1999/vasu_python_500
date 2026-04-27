class emp :
    def setEmp(self):
        print("enter emp info : ")
        self.name=input("enter name : ")
        self.id=int(input("enter id : "))
        self.salary=float(input("enter salary : "))

    def getEmp(self):
        print("\nemp info : ") 
        print("emp name : ",self.name)   
        print("emp id : ",self.id)   
        print("emp salary : ",self.salary)  
        print("---------------------------")



e1= emp()
e2= emp()
e3= emp()


e1.setEmp()
e2.setEmp()
e3.setEmp()

e1.getEmp()
e2.getEmp()
e3.getEmp()



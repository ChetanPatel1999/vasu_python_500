class emp :
    def setEmp(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def getEmp(self):
        print("\nemp info : ") 
        print("emp name : ",self.name)   
        print("emp id : ",self.id)   
        print("emp salary : ",self.salary)  
        print("---------------------------")

n = int(input("enter no of employ : ")) # 3
employs = []    

#create object and append in list
for i in range(n):
    employs.append(emp())

# set data in all object store in list
for e in employs:
     print("enter emp info : ")
     name=input("enter name : ")
     id=int(input("enter id : "))
     salary=float(input("enter salary : "))
     e.setEmp(id,name,salary)


for e in employs:
    e.getEmp()    





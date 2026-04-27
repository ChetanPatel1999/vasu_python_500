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

n = int(input("enter no of employ : ")) # 3
employs = []    

#create object and append in list
# for i in range(n):
#     obj = emp()
#     employs.append(obj)

for i in range(n):
    employs.append(emp())

# set data in all object store in list
for e in employs:
    e.setEmp()


for e in employs:
    e.getEmp()    





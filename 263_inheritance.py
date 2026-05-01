class student:
    def setStudent(self,name,rno,fees):
        self.name=name
        self.rno=rno
        self.fees=fees
    def getStudent(self):
        print("student info : ")
        print("name :",self.name)    
        print("rno :",self.rno)    
        print("fees :",self.fees)    


class engStd(student):
    def setEng(self,sem,branch):
        self.sem=sem
        self.branch=branch
    def getEng(self):
        print("sem :",self.sem)    
        print("branch :",self.branch) 
        print("------------------------")   

class mediStd(student):
    def setmedi(self,prof,speci):
        self.prof=prof
        self.speci=speci
    def getmedi(self):
        print("prof :",self.prof)    
        print("speci :",self.speci) 
        print("------------------------")   

s1= engStd()
s1.setStudent("ram",101,45000)
s1.setEng(5,"CS")
s1.getStudent()
s1.getEng()


s2= mediStd()
s2.setStudent("manthan",102,120000)
s2.setmedi(3 ,"artho")
s2.getStudent()
s2.getmedi()
      
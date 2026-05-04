class student:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def display(self):
        print("student info : ")
        print("name : ",self.name)    
        print("rno : ",self.rno)    

class eng(student):
    def __init__(self,name,rno,sem,branch):
        super().__init__(name,rno)
        self.sem=sem
        self.branch=branch
    def display(self):
        super().display()
        print("sem : ",self.sem)
        print("branch : ",self.branch)
       
s1=eng("ram",101,4,"CS")
s1.display()
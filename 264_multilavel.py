class student:
    def setRno(self,rno):
        self.rno=rno
    def getRno(self):
        print("rno : ",self.rno)    

class marks(student):
    def setMarks(self,hindi,math):
        self.hindi=hindi
        self.math=math
    def getMarks(self):
        print("hindi : ",self.hindi)    
        print("math : ",self.math)    

class result(marks):
    def getResult(self):
        per=(self.hindi+self.math)/2
        print("percentage : ",per)


s1 = result()
s1.setRno(101)
s1.setMarks(20,80)
s1.getRno()
s1.getMarks()
s1.getResult()

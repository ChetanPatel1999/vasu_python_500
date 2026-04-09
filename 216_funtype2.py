# Keyword arguments  
def dipslayStudent(name, rno, per):
    print("student info : ")
    print("name : ",name)
    print("rno : ",rno)
    print("per : ",per)
    print("-------------")


dipslayStudent(rno=101,name="ram",per=45.67)   # keyword-argument
dipslayStudent("ram",per=45.78,rno=102)   # keyword-argument


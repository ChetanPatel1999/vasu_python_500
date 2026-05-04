class addition:
    def add(self ,a,b):
        c=a+b
        print("add = ",c)

class multiplication:
    def multi(self, a,b):
        c=a*b
        print("mult = ",c)

class calculator(addition,multiplication):
    pass

c1=calculator()
c1.add(12,45)

c1.multi(12,5)
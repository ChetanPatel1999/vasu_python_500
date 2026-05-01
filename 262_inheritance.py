class A:
    def m1(self):
        print("A m1 method is called")

class B(A):
    def m2(self):
        print("B m2 method is called")

o1=B()
o1.m1()
o1.m2()



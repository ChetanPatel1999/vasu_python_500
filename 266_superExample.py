# method overriding: when a child class have a method which name and no of parameter same
                    #  as  parent class method so this situation called method overriding.
   
#super() : super function is used to call base class methods in derived class.

class base:
    def display(self):
        print("hi i am base display")

class derived(base):
    def display(self):   # method override
       super().display()
       print("hi i am derived display")


obj=derived()
obj.display()

# we can call a function inside other funtion
def fun1():
    print("hello i am fun1")

def fun2():
    fun1()
    print("hello i am fun2")

def fun3():
    print("hello i am fun3") 
    fun2()

fun3()
print("fun calling is end")    

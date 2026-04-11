# wap to print a msg 5 times using recursion.
i=1
def fun():
    global i
    print("hello world institue") # 4
    i+=1 # 5
    if i<=5:
     fun()   

fun()    
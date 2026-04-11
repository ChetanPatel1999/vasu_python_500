#wap to print 1 to 15 numbers using recursion
i=1
def fun():
    global i
    print(i ,end=" ") 
    i+=1
    if i<=15:
     fun()   

fun()    
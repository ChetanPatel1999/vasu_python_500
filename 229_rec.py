#wap to print 1 to  n  numbers using  recursion.
def fun(num):
    if num>1:
      fun(num-1)   
    print(num) 

fun(10)    
#wap to print number given number to 1 in reverse order using recursion
def fun(num):
    print(num ,end=" ") 
    if num>1:
     fun(num-1)   


fun(20)    
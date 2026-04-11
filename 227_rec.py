#wap to print 1 to 15 numbers even numbers using recursion
i=1
def table(num):
    global i
    print(f"{num} x {i} = {num*i}")
    i+=1
    if i<=10:
     table(num)   


table(5)   

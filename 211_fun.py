#function with paramter and with return value 
def add(a,b):
    c=a+b
    return c



print( add(6,18) )

print(f"my addition ans is = {add(7,9)}")

res = add(12,10)    
print("addition = ",res) 

res = add(120,10)  
print("sum = ",res) 


a=add(1,10)   
print("res = ",a) 


if add(44,20) >25 :
    print("ans is greter then 25")
else:
    print("ans is less then 25")    

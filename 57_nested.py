# Wap to find greatest number among has given three numbers without 
# using logical and operator.
num1=int(input("enter a num1 : "))
num2=int(input("enter a num2 : "))
num3=int(input("enter a num3 : "))
if num1>num2:
    if num1>num3:
        print("greatest num : ",num1)
    else:
        print("greatest num : ",num3)
else:
     if num2>num3:
         print("greatest num : ",num2) 
     else:
         print("greatest num : ",num3)              

# Write a program to find greatest number among has given three numbers.
num1=int(input("enter a num1 : "))
num2=int(input("enter a num2 : "))
num3=int(input("enter a num3 : "))
if num1>num2 and num1>num3:
    print("greatest num : ",num1)
elif num2>num3:
    print("greatest num : ",num2)
else:
    print("greatest num : ",num3)     

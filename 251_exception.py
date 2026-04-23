num= int(input("enter a num : "))#-5
try :
    if num<0:
      raise ValueError("nagative value error")
    print("value of number : ",num)
except ValueError as v:
    print(v)


print("addition app : ")
a=int(input("enter a  : "))
b=int(input("enter b  : "))
c=a+b
print("addition : ",c)
print("programm run succefully")
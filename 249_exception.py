# one try with multiple except block
print("program is start ....")
try:
  a=int(input("enter a  : "))
  b=int(input("enter b  : "))
  c=a/b
  print("division : ",c)
except ZeroDivisionError:
  print("zero division error")  
except ValueError:
  print("invalid input")  
  
print("programm run succefully")


print("addition app : ")
a=int(input("enter a  : "))
b=int(input("enter b  : "))
c=a+b
print("addition : ",c)
print("programm run succefully")

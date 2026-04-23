print("program is start ....")
try:
  a=int(input("enter a  : "))# 12
  b=int(input("enter b  : "))# 7
  c=a/b
except ZeroDivisionError:
  print("zero division error")
else:
  print("division : ",c)  
finally:
  print("finally always run")  
print("programm run succefully")

print("addition app : ")
a=int(input("enter a  : "))
b=int(input("enter b  : "))
c=a+b
print("addition : ",c)
print("programm run succefully")

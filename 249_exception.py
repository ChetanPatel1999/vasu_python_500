# one try with multiple except block
print("program is start ....")
l1=[12,34,56,78,90]
print(l1)
try:
  index= int(input("enter index : ")) # 25
  print("element at given index : ",l1[index])
  a=int(input("enter a  : "))  # 13
  b=int(input("enter b  : ")) # 0
  c=a/b
  print("division : ",c) # 3.2
except ZeroDivisionError:
  print("zero division error")  
except ValueError:
  print("invalid input")  
except IndexError:
  print("invalid index")    
except:
  print("something wrong")
  
print("programm run succefully")


print("addition app : ")
a=int(input("enter a  : "))
b=int(input("enter b  : "))
c=a+b
print("addition : ",c)
print("programm run succefully")

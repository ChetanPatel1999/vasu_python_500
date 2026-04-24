l1=[12,34,56,78]
index=int(input("enter a index : "))
try:
    if index >= len(l1):
      raise ValueError("invalid integer")
except ValueError as v:
   print(v)
else:
   print("element at given index : ",l1[index])

print("program run succefully")   


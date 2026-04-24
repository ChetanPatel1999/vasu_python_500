def product(a,b):
    print("function start ....")
    try:
      if not isinstance(a,int) or not isinstance(b,int):
         raise TypeError("non integer values")
    except TypeError as t:
       print(t)
    else:
       return a*b   
       

    

ans = product(12,"hello")
print(ans)
print("program run succefully")




#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# we are also allowed to extract the values back into variables. This is 
# called "unpacking":  
t1=(23,45,67)
print(t1)
a,b,c=t1
print(a)
print(b)
print(c)

*r,s=t1
print(r)
print(s)


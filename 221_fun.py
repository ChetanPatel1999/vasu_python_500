#call by reference
def fun(a):
    print("a = ",a)# [90,78,34,56]
    a[3]=700
    print("a = ",a)# [90,78,34,700]



num=[90,78,34,56]
print("num = ",num) # [90,78,34,56]
fun(num)
print("num = ",num) # [90,78,34,700]
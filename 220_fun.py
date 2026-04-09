#pass by value
def fun(a):
    print("a = ",a)# 90
    a=70
    print("a = ",a)# 70



num=90
print("num = ",num) # 90
fun(num)
print("num = ",num) # 90

# Write a program to takes a number as input and calculates the sum of its 
# individual digits.
num=int(input("enter a num : "))#342
res=0
while num>0:
    rem=num%10 # 3
    res=res+rem #9
    num=num//10 # 0
print(f"sum of individul digit : {res}")    
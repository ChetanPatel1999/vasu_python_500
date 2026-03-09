# .Write a program to check given number is perfact or not. 
num=int(input("enter a num : "))#6
sum=0
for i in range(1,num+1):
    if num%i==0:
       sum=sum+i
if sum==num*2:
    print("num is perfact")
else:
    print("num is not perfact")         
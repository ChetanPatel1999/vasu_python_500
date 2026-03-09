# . Write a program to check given number is prime or not.
num=int(input("enter a num : "))#15
count=0
for i in range(1,num+1):
    if num%i==0:
       count+=1
if count==2:
    print("num is prime")
else:
    print("num is not prime")         
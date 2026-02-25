#  Write a program to check given number is perfact or not.
num=int(input("enter a num : "))#6
i=1
sum=0
while i<=num:
    if num%i==0:
        sum=sum+i
    i+=1
if sum==num*2:
    print("num is perfact")
else:
    print("num is not perfact")      
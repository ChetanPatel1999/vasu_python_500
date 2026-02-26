# . Write a program that takes a number as input and displays its digits in 
# reverse order as a new number.
num=int(input("enter a num : "))#835
rev=0
while num>0:
    rem=num%10 
    rev=rev*10+rem # 
    num=num//10 
print("reverse num : ",rev) 
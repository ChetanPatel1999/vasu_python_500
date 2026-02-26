# Write a program to that takes a number as input and calculates the sum of 
# only its even digits. 
num=int(input("enter a num : "))#5324
sum=0
while num>0:
    rem=num%10
    if rem%2==0:
        sum=sum+rem
    num=num//10 
print(f"sum of only even digit in given number : {sum}")    
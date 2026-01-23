# Write a program to find sum of individuals digits of any three digits 
# number.
num=int(input("enter a 3 digit num : "))
r=num//100
s=(num%100)//10
t=num%10
sum=r+s+t
print(f"sum of individual digit : {sum}")
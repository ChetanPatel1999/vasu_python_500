# Write a program to find sum of individuals digits of any three digits 
# number.
num=int(input("enter a 3 digit num : "))
r=num//100
s=(num%100)//10
t=num%10
sum=r+s+t
rev=r+s*10+t*100
print(f"sum of individual digit : {sum}")
print(f"reverse num : {rev}")
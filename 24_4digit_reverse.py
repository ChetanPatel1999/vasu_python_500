#  Write a program to find sum of individuals digits of any four digits 
# number.
num= int(input("enter 4 digit num : "))
r=num//1000
s=(num%1000)//100
t=(num%100)//10
u=num%10
# print("reverse number : ",u,t,s,r,sep="")
rev=r+s*10+t*100+u*1000
print("reverse num :",rev)


#  Write a program to check given number is prime or not.
num=int(input("enter a num : "))#12
i=1
c=0
while i<=num:
    if num%i==0:
        c=c+1
    i+=1
if c==2:
    print("num is prime")
else:
    print("num is not prime")      
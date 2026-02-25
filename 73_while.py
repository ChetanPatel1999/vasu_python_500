#  Write a program to count factors of given number.
num=int(input("enter a num : "))#12
i=1
c=0
while i<=num:
    if num%i==0:
        c=c+1
    i+=1
print("total factors count = ",c)    
# Write a program to display even number 1 to n (given number).
num=int(input("enter a num : "))#11
for i in range(1,num+1):
    if i%7==0:
        print(i,end=" ")
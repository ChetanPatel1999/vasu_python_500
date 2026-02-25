# . Write a program to display even number series. 
num=int(input("enter a num : "))
i=1
while i<=num:
    if i%2==0:
        print(i,end=" ")
    i=i+1 
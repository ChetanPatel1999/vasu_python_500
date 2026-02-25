#  Write a program to display factors of given number.
num=int(input("enter a num : "))#15
i=1
print(f"factors of {num} = ",end="")
while i<=num:
    if num%i==0:
        print(i,end=" ")
    i+=1
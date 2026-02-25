# . Write a program to display sum 1 to n ( given number).
num=int(input("enter a num : "))#10
i=1
sum=0
while i<=num:
    sum=sum+i 
    i+=1
print(f"sum of 1 to {num}  = ",sum)    
print(f"avearge of 1 to {num}  = ",sum/num)    
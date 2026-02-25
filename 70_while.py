#  Write a program to display sum 1 to n  ( given number) only even numbers 
# sum. 
num=int(input("enter a num : "))#10
i=1
sum=0
while i<=num:
    if i%2==0:
        sum=sum+i 
    i+=1
print(f"sum of 1 to {num} only even numbers  = ",sum)    

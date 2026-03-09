# Write a program to display sum  1 to n (given number).
num=int(input("enter a num : "))#10
res=0
for i in range(1,num+1):
    res=res+i #21
print(f"total sum 1 to {num} = {res}")        
print(f"total average 1 to {num} = {res/num}")        
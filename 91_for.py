# Write a program to display sum  1 to n  only even numbres.
num=int(input("enter a num : "))#10
res=0
for i in range(1,num+1):
    if i%5==0:
        res=res+i 
print(f"total sum 1 to {num} = {res}")    
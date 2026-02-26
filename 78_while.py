#  Write a program that takes a number as input and counts how many digits 
# it contains.
num=int(input("enter a num : "))#78
count=0
while num>0:
    count=count+1 
    num=num//10 
print(f"total digit count : {count}")    
# . Write a program to find the maximum element in an array.
l1=[2355,45,6,2,78,6]
max=l1[0]
for num in l1:
    if max<num:
        max=num

print("max = ",max)        
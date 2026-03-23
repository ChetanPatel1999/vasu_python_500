#  Write a program to print make a new list which contain element square of input list.
l1=[4,2,5,6,7,8,3]

print("list element are : ")
for num in l1:
    print(num,end=" ")

squares=[]
for num in l1:
    squares.append(num**2)

print("\nlist element square are : ",squares)

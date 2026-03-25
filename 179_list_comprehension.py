# List comprehension offers a shorter syntax when you want to create a new list based 
# on the values of an existing list.


# l1=[3,5,2,6,7]
# squares=[]
# for num in l1:
#     square=num*num
#     squares.append(square)

# print(l1)
# print(squares)

# l1=[3,5,2,6,7]

# squares=[num*num for num in l1]

# l2=[num+5 for num in l1]

# print(l1)
# print(squares)
# print(l2)


# l1=[3,5,2,6,7,8]
# evenNum=[]
# for num in l1:
#     if num%2==0:
#         evenNum.append(num)

# print(l1)
# print(evenNum)

# l1=[3,5,2,6,7,8]

# evenNum=[num for num in l1 if num%2==0]

# oddNum=[num for num in l1 if num%2==1]

# print(l1)
# print(evenNum)
# print(oddNum)


# l1=[3,12,2,16,7,8,60,34]

# # l2=[num for num in l1 if num%4==0]

# # l2=[num for num in l1 if num>10]
# # l2=[num for num in l1 if num>10 and num<20]

# l3=[12,2,60]
# l4=[num for num in l1 if num not in l3 ]

# print(l1)
# print(l4)

# l1=[456,789,342,56567,767,444]

# l2=[num for num in l1 if '4' in  str(num)]


# print(l1)
# print(l2)

# l1=[num for num in range(1,11)]
# print(l1)

l1=[num for num in range(1,11) if num%2==0]
print(l1)

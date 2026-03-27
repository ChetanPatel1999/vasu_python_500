#. Write a program to reverse all elements of an list  without using any extra list.

# l1=[12,34,56,78,90]

# l2= l1[::-1]
# l2=[]

# for i in range( len(l1)-1 , -1, -1): # 3
#     l2.append(l1[i])

# for i in range( 1 , len(l1)+1): # 1 2 3 4 5
#     l2.append(l1[-i])


l1=[12,34,56,78,90,55,77,88]
   # 0  1  2 3  4
print(l1)

for i in range(len(l1)//2):  # 0 1 2 3
    temp=l1[i] # 12
    l1[i]=l1[-(i+1)] # 90
    l1[-(i+1)]=temp

print(l1)


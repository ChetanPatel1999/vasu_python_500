#how to take list element from user
l1=[]
n=int(input("enter list length : "))#5
# for i in range(n):
#     num=int(input(f"enter list num{i+1} : "))
#     l1.append(num)

for i in range(n):
    l1.append(int(input(f"enter list item{i+1} : ")))


print("input list : ",l1)
#wap to take a list from user and display in reverse order.
l1=[]
n=int(input("enter list length : "))#5

for i in range(n):
    l1.append(int(input(f"enter list item{i+1} : ")))


print("input list : ",l1)

# reverse=l1[::-1]

reverse=[]
# 3,5,6,7,9
for i in range(len(l1)-1, -1, -1):# 4,3,2,1,0
    reverse.append(l1[i])
         


print("reverse list : ",reverse)
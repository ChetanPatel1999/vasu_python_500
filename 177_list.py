# wap to conut frequency of each element in list
l1=[3,5,4,3,6,5,7,3,4,3]
l2=[]
for num in l1: # 3
    c=0
    if num not in l2:
        for n in l1:# 6
            if num==n:
                c+=1
        print(f"{num} is appear {c} times") 
        l2.append(num)       
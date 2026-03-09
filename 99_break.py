# wap to find/search a given elenet in list.
l1=[34,67,23,78,55,66,7,3,56,67]   # length :10
num=6
isFind=False
for i in l1:
    if i==num:
        isFind=True
        break

if isFind==True:
    print("num is find")
else:
    print("num is not find")    
    
    

#  Write a program to check how many digits at each index of array. 
l1=[345 ,67 , 7896  , 4 , 12342]
#  index:0 , total digit: 3
#  index:1 , total digit: 2
c=0
for num in l1:
    print(f"index:{c} , total digit:{len(str(num))}")
    c+=1

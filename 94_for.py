# . Write a program to display factors count of given number.
# 15 :- 1 3 5 15  => 4
# 14 :-1 2 7 14
num=int(input("enter a num : "))#15
count=0
for i in range(1,num+1):
    if num%i==0:
       count+=1
print("total factors : ",count)       
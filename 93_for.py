# . Write a program to display factors of given number.
# 15 :- 1 3 5 15  => 4
# 14 :-1 2 7 14
num=int(input("enter a num : "))#15
print(f"factor of {num} :",end="")
for i in range(1,num+1):
    if num%i==0:
       print(i,end=" ")# 1 3 5 15
# . Write a program to input elements into an list and divide them into two separate list — one 
# containing even numbers and the other containing odd numbers.
l1=[4,6,3,2,8,9]
even=[]
odd=[]
for num in l1:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)

print("input list : ",l1)            
print("even list : ",even )            
print("odd list : ",odd)            
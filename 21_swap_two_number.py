#. Write a program to swap any two numbers using third variable. 
a=int(input("enter a : "))
b=int(input("enter b : "))
print("values before swapping : ")
print("a =",a)
print("b =",b)

c=a
a=b
b=c

print("values after swapping : ")
print("a =",a)
print("b =",b)
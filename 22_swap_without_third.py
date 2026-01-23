#. Write a program to swap any two numbers whithout using third variable. 
a=int(input("enter a : "))
b=int(input("enter b : "))
print("values before swapping : ")
print("a =",a)
print("b =",b)

# a=a+b
# b=a-b
# a=a-b

#by using python multiple value assign techniqe
a,b=b,a

# a=a*b
# b=a/b
# a=a/b

print("values after swapping : ")
print("a =",a)
print("b =",b)
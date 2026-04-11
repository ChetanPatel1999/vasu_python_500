#lambda function in python
# lambda function is one line function

# def add(a,b):
#     return a+b

add = lambda a,b : a+b

cube = lambda num : num*num*num

CircleArea=  lambda radius : 3.141 * radius*radius

evenOdd = lambda num : "even" if num%2==0 else "odd"

geatestNum = lambda a,b : a if a>b else b

geatestNum1 = lambda a,b,c : a if a>b and a>c else b if b>c else c

evenList= lambda l1 : [i for i in l1 if i%2==0 ]


l1=[1,2,3,4,5]
l2 = evenList(l1)
print(l2)


print(geatestNum1(120,800,800))

# print(evenOdd(9))

# print(CircleArea(6.3))

# print(cube(4))
# print(add(12,5))
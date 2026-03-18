# .   Write a program to reverse each word in a string without changing their order. 
s="hello my name is chetan patel"
l1=s.split()
n=""
for word in l1:
    n=n+word[::-1]+" "
print(s)
print(n)

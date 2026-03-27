#if you want to change tuple value
#so frist convert tuple in list
#then chnage in list
#then again change list in tuple

t1=(23,45,67,78,9)

l1=list(t1)

l1[2]=500
l1.append(1000)
t1=tuple(l1)

print(t1)
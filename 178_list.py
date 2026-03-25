l1=[3,4,5,3,6,5,4,3,6,7,3]
# print(l1.count(7))
l2=[]
for num in l1:
  if num not in l2:
    print(f"{num} is appear {l1.count(num)} times")
    l2.append(num)
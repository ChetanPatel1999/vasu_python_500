#  Write a program to count how many times each character appears in a string using 
# dictionary.
# s="hello world institute"

# l1=[]
# for char in s:   
#    c=0
#    if char not in l1:
#     for shar in s:
#         if char==shar:
#             c+=1
#     print(f"{char} is apper {c} times") 
#     l1.append(char)   
# 

# s="hello world institute"
# l1=[]
# for char in s:   
#    if char not in l1:
#     print(f"{char} is apper {s.count(char)} times") 
#     l1.append(char)     

s="hello world institute"
d1={}  #{'h':1,"e":1,'l':2,'o':1," ":1}
for char in s:
  if char != " ":  
    if char not in d1:
        d1[char]=1
    else:
        d1[char]=d1[char]+1   

print(s)
# print(d1)
for key in d1:
   print(f"{key} is appear {d1[key]}")

      
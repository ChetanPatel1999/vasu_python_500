#wap to take a string from user and make a string which have only uniqe eliment from given string.
s1= "aabbacdcda"
s2= "xxbbyyczcdl"
s3=s1+s2
newstr=""  #abcd
for char in s3:  # a
    if char not in newstr:
        newstr=newstr+char # ab

print("string1 : ",s1)
print("string2 : ",s2)
print("uniqe : ",newstr)







# print(s)
# s1=set(s)
# print(s1)
# newstr=""
# for char in s1:
#     newstr=newstr+char

# print(newstr)
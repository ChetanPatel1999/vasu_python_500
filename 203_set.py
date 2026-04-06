# Check if two sets are equal.

s1={3,4,2,5}
s2={4,3,5,2}

if s1.issubset(s2) and s2.issubset(s1):
    print("set is sem")
else:
    print("set is differnt")    



# if len(s1)!=len(s2):
#     print("set is different")
# else:
#     for num in s1:
#         if num not in s2:
#             print("set is different")
#             break
#     else:
#         print("set is sem")        

    
# if s1==s2:
#     print("set is same")
# else:
#     print("set is difference")    
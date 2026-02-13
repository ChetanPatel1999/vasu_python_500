# Write a program to accept a number and check it is multiple of 3,5,8 or multiple of 
# 3,5 or multiple of 5,8 or multiple of 3,8 or only multiple of 3 or only multiple of 5 or 
# only multiple of 8  or not multiple of 3,5,8.
num=int(input("enter a num : "))#120
if num%3==0 and num%5==0 and num%8==0:
    print("multiple of 3,5,8") 
elif num%3==0 and num%5==0:
     print("multiple of 3,5")  
elif num%3==0 and num%8==0:
     print("multiple of 3,8")
elif num%8==0 and num%5==0:
     print("multiple of 8,5")
elif num%3==0:
     print("multiple of 3") 
elif num%5==0:
     print("multiple of 5")
elif num%8==0:
     print("multiple of 8")
else:
     print("not multiple of 3,5,8")                                       
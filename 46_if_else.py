#  Write a program to check whether a character is an uppercase  so convert in lower 
# case or lowercase so convert in uppercase char .
alpha=input("enter a alpha : ")# B
if alpha>='A' and alpha<='Z':
    alpha= chr(ord(alpha)+32)
    print("lower case : ",alpha)
else:
    alpha= chr(ord(alpha)-32)
    print("uper case : ",alpha)

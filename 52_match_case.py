#Write a program to make simple calculator. 
#       Press 1 to addition 
#       Press 2 to subtraction 
#       Press 3 to multiplication 
#       Press 4 to division
print("<--------welcome to my calculator----->")
print("       press 1 for addition")
print("       press 2 for subtraction")
print("       press 3 for multiplication")
print("       press 4 for division")
num=int(input("       choose any option : "))

match num:
    case 1:
        print("you choosed addition ...")
        a=int(input("enter first num : "))
        b=int(input("enter second num : "))
        c=a+b
        print("addition : ",c)
    case 2:
        print("you choosed subtraction ...")
        a=int(input("enter first num : "))
        b=int(input("enter second num : "))
        c=a-b
        print("subtraction : ",c)  
    case 3:
        print("you choosed multiplication ...")
        a=int(input("enter first num : "))
        b=int(input("enter second num : "))
        c=a*b
        print("multiplication : ",c)   
    case 4:
        print("you choosed division ...")
        a=int(input("enter first num : "))
        b=int(input("enter second num : "))
        c=a/b
        print("division : ",c) 
    case _ : print("wrong input! please enter 1 to 4")      
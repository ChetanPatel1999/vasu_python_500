#how to take dictionary key value from user
d1={}
# num= int(input("enter total num of student : "))#5
# for i in range(num):
#     key=input("enter name : ")
#     value= int(input("enter age : "))
#     # d1[key]=value
#     d1.update({key:value})

# num= int(input("enter total num of student : "))#5
# for i in range(num):
#     # d1[key]=value
#     d1.update({input("enter name : "):int(input("enter age : "))})



while True:
    d1[input("enter name : ")]=int(input("enter age : "))
    num=int(input("press 1 for more student entry : "))#2
    if num!=1:
        break
   
print(d1)


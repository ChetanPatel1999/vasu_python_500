# s=input("enter name : ")
# file=open(r"C:\Users\PC\Desktop\mayank\abc.txt","a")
# file.write(s+"\n")
# file.close()

# writelines :- write list using write line method
file = open(r"C:\Users\PC\Desktop\mayank\abc.txt","w")
fruits=["apple\n","banana\n","mango\n","grapus\n"]
file.writelines(fruits)
file.close()
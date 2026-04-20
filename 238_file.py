num= int(input("enter a num : "))
cube= num*num*num
print(f"cube of {num} = {cube}")
file = open(r"C:\Users\PC\Desktop\mayank\cube.txt","a")
file.write(f"cube of {num} = {cube}\n")
file.close()
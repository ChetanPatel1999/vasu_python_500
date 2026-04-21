# image copy using python
#  rb :- rb mode is used to open binary file
file=open(r"C:\Users\PC\Desktop\mayank\fox.jpg","rb")
data= file.read()
# print(data)
file.close()


file=open(r"C:\Users\PC\Desktop\chetan\myfox.jpg","wb")
file.write(data)
file.close()

print("image copy succefully")
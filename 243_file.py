# how to read data from file
file=open(r"C:\Users\PC\Desktop\mayank\cube.txt","r")
# data = file.read(3)  # read only 3 char from file   
# data= file.readline()   # its read sigle line from file
# print(data)
# data= file.readline()
# print(data)

data= file.readlines()
print(data)

for line in data:
    print(line)
file.close()
# how to read data from file
file=open(r"C:\Users\PC\Desktop\mayank\cube.txt","r")
data = file.read()
print(data)

data= data.split()

c=0
for word in data:
    if "cube"==word:
        c+=1
    print(word)

print("total cube word inside file : ",c)    
file.close()
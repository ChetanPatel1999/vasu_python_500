# operation 1.
# open(r"C:\Users\PC\Desktop\mayank\stdent_grade.txt","x")




# operation 2.
# file = open(r"C:\Users\PC\Desktop\mayank\stdent_grade.txt","w")
# #id,name,stream,gread
# student_data=["01,ram sharma,CS,A+\n" ,"02,shyam sharma,EC,B+\n","03,mahesh sharma,AI/ML,C+\n"]
# file.writelines(student_data)
# file.close()

# operation 3.
# file = open(r"C:\Users\PC\Desktop\mayank\stdent_grade.txt","r")
# for i in range(20):
#     data= file.readline()
#     if data:
#          print(data)
#     else:
#          break     
#     input()
# print("fetch all data sufully")    
# file.close()

#operation 4.
file = open(r"C:\Users\PC\Desktop\mayank\stdent_grade.txt","r")
data= file.readlines()
new_list=[]
for line in data:
    if "mahesh" in line:
        new_list.append("03,mahesh sharma,Art,C+\n")
    else:
        new_list.append(line) 

file.close()
file = open(r"C:\Users\PC\Desktop\mayank\stdent_grade.txt","w")
file.writelines(new_list)
file.close()




#operation 5.
# file = open(r"C:\Users\PC\Desktop\mayank\stdent_grade.txt","a")
# file.write("04,rajat sharma,DSA,C")
# file.close()
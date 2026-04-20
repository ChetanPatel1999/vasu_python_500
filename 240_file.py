# how to create file and write data inside file
# "w" :- open file as write mode and delete file existing data and
# write new data

# "a" :-  append mode also create file/open file but its
# not delete privius data of file its append only new data
# file = open(r"C:\Users\PC\Desktop\mayank\abc.txt","w")

# "x" :-  x mode is used only create file 
# open(r"C:\Users\PC\Desktop\mayank\xyz.txt","x")


file = open(r"C:\Users\PC\Desktop\mayank\abc.txt","a")
file.write("hello i am chetan\n")
file.close

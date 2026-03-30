# Write a program to copy one dictionary into another dictionary. 
stn={"pen":10 , "book": 50, "color":20}
d1={}

for key in stn:
     d1[key]=stn[key]+10


print(stn)
print(d1)     


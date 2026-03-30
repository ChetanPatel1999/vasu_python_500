# Write a program to clear all elements of a dictionary.
stn={"pen":10 , "book": 50, "color":20}
while stn:
    print(stn.popitem())


print(stn)
# check a given data exist in dictionary as value or not
stn_item={"pen":10 , "book": 50, "color":20}

# print(5 in stn_item.values())
data=5
for key in stn_item:
    if stn_item[key]==data:
        print("data is exist as a value in dict")
        break
else:
    print("data is not exist as value in dict")    

# if "book" in stn_item:
#     print("book is exist as key in dict")
# else:
#     print("book is not exist as key in dict")    
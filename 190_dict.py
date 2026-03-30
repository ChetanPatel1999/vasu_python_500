#update method
#pop()
#popitem()
stn={"pen":10 , "book": 50, "color":20}

# stn["book"]=60
# stn.update({"book":60})

# stn["pencial"]=5
# stn.update({"pencial":5})
# stn.update({"pencial":5,"cover":100})
print(stn)
# stn.pop("book")
# del_value=stn.pop("book")
# print(del_value)

# res= stn.popitem()   #its remove last item from dictionary
# print(res)

# del stn // delete dictionary

# stn.clear()    its delete all element of dictionary

del stn["pen"]
print(stn)
#Variable-Length Arguments  
#**kwargs - These are Keyword Arguments. 

# def disp(**data):
#     print(data)
#     for ky in data:
#         print(ky,"=",data.get(ky))



# disp(name="ram",age=45,village="takwasa")


# def disp(*a,**data):
#     print(data)
#     print(a)
#     for ky in data:
#         print(ky,"=",data.get(ky))



# disp(12,34,56,name="ram",age=45,village="takwasa")



def disp(b,*a,**data):
    print(data)
    print(a)
    print(b)
    for ky in data:
        print(ky,"=",data.get(ky))



disp(12,34,56,name="ram",age=45,village="takwasa")
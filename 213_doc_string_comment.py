#sigle line comment
"its also sigle line comment"
'its also sigle line comment'
"""
its 
multline 
comment
"""

# docstring comment

def add():
    "this function perform addition"
    a=12
    b=5
    c=a+b
    print("addition : ",c)

def myFun():
    a=12
    b=8
    c=a+b
    return c

res=myFun()
print(res)


add()  
print(add.__doc__)  

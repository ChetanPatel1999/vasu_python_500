# in python we can return multiple value using return stmnt
# its return maultiple value in form of tuple data
def operation(num):
    cube=num*num*num
    square= num*num
    return cube,square,"home",[1,2,3]

res=operation(5)
print(res)
print("cube : ",res[0])
print("square : " ,res[1])
print("string : " ,res[2])
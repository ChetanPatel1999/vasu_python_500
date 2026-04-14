import random
import string

# res= string.ascii_letters
# res= string.ascii_lowercase
# res= string.ascii_uppercase
# res= string.digits
# print(res)

def generatePassword():
    s=string.ascii_letters+string.digits
    pass1=""
    for i in range(6):
        pass1=pass1+random.choice(s)
    return pass1


ranpass= generatePassword()
print("randome password : ",ranpass)
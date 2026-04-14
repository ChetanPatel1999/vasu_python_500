# import calculator

# calculator.add(12,6)
# calculator.mul(12,4)
# calculator.sub(12,4)
# calculator.div(12,4)

# import calculator as cl

# cl.add(12,5)
# cl.sub(20,5)


# how to import from a module individual function
# from calculator import add

# add(12,6)


# # how to import from a module multiple  function
# from calculator import add,sub

# add(12,6)
# sub(5,7)

# # how to import from a module all function
# from calculator import *

# add(12,6)
# sub(5,7)
# mul(4,6)



# how to import from a module individul function using alice 
# from calculator import add as a ,sub as s

# a(12,6)
# s(15,9)



# # we can import multiple module using sigle import stmnt
# import calculator,greeting

# calculator.add(12,6)
# greeting.greet1()

# # we can import multiple module using sigle import stmnt
# import calculator as cl,greeting as gr

# cl.add(12,6)
# gr.greet1()


# we can import multiple module using sigle import stmnt
from calculator import add,s  
from greeting import greet1

add(12,6)
greet1()
print(s)
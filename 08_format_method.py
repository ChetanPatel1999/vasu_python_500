#display data using format method of string
a=120
b=50
c=a+b
name="raj varma"
city="indore"
cm=5.7

print("value of a = {}".format(a))
print("value of b = {}".format(b))
print("sum of {} and {} = {}".format(a,b,c))
print("sum of {0} and {1} = {2}".format(a,b,c))
print("sum of {0} and {0} = {0}".format(a,b,c))
print("sum of {x} and {y} = {z}".format(x=a,y=b,z=c))
print("my birth place is {0} and my collage situted in {0}".format(city))
print("distance = {} cm".format(cm))


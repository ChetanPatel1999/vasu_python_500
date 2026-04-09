# Variable-Length Arguments  non keyword type
def add(b,*a):   # *a :- variable length argument
    sum=0
    for num in a:
        sum=sum+num
    print("sum = ",sum) 
    print("b = ",b)   
   



add(12,5)
add(12,5,7)
add(12,5,7,23)
add(12,5,7,23,12)

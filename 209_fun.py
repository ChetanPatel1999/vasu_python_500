# function with parameter
def cube(num):
    res= num*num*num
    print("       cube of",num,"=",res)

def rangeCube(s,e):
    print(f"<--- cube range {s} to {e} --->")
    for i in range(s,e+1): 
        cube(i) 
        print("      -----------------")  
    


rangeCube(1,5)
rangeCube(7,9) 
rangeCube(11,15) 

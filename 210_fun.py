#function calling with paramter 

def greatestNum(a,b):
    if a>b:
        print(f"greatest num : {a}")
    else:
         print(f"greatest num : {b}")

def table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

def evenOdd(num):
    if num%2==0:
        print("even num")
    else:
        print("odd num ")   



evenOdd(15)

# table(7)


# greatestNum(12,67)
# greatestNum(125,67)
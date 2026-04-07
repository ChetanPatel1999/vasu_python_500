def greatestNum(a,b):
    if a>b:
        return a
    else:
        return b



def evenOdd(num):
    if num%2==0:
        return "even num"
    else:
        return "odd num "     

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact    

def listSum(list1):
    sum=0
    for i in list1:
        sum+=i
    return sum    



l1=[4,5,11,10]
res= listSum(l1)
print(res)

# res= factorial(5)
# print("factorila = ",res)

# print(evenOdd(34))
# print(evenOdd(7))


# res=greatestNum(12,78)
# print("great num : ",res)
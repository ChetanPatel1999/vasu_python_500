#wap to find a digit in given number.
num= int(input("enter  a num : "))# 6987459   
digit = int(input("enter  a digit : "))# 9

while num>0:
    rem=num%10
    if digit==rem:
        print("digit is found")
        break
    num=num//10
else:
    print("digit is not found")



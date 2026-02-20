#  ATM Withdrawal – If account type is Savings or Current (choose with 
# switch), check if balance is enough before withdrawal. (nested switch).
print("welcome to HDFC bank ATM!")
print("select account type : ")
print("1. saving account ")
print("2. currunt account")
select=int(input("select : "))
match select:
    case 1:
        print("you select saving account ! ")
        amount=int(input("enter amount : "))
        if amount<=50000:
            print("suffician balence for withdral")
        else:
            print("not suffician balence for withdral")   

    case 2:
        print("you select current account ! ")
        amount=int(input("enter amount : "))
        if amount<=200000:
            print("suffician balence for withdral")
        else:
            print("not suffician balence for withdral")    
           
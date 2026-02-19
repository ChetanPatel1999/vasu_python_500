# Mini Project Task:

age=int(input("enter your age : "))#34
if age>=18:
    print("welcome to my club !")
    print("club menue : ")
    print("1. sandwitch : 150")
    print("2. burger : 80")
    print("3. pasta : 100")
    order=int(input("choose your order : "))
    match order:
        case 1: 
            print("select sandwith type : ")
            print("1. paneer sandwitch")
            print("2. masala sandwitch")
            print("3. cheez sandwitch")
            type=int(input("select type : "))
            match type:
                case 1: print("your paneer sandwitch is ordered please pay 150 rs")
                case 2: print("your masala sandwitch is ordered please pay 150 rs")
                case 3: print("your cheez sandwitch is ordered please pay 150 rs")
                case _: print("invalid choise please press 1-3")
        case 2: print("your burger is ordered please pay 80 rs")
        case 3: print("your pasta is ordered please pay 100 rs")
        case _: print("invalid choise please press 1-3")
else:
    print(f"sorry you are not allowed please try after {18-age} year")    
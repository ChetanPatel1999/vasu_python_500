#wap to print state full name according to state short name
stateShortName=input("enter state short name : ")
match stateShortName:
    case "mp" | "MP":print("madhya-pradesh")
    case "rj":print('rajsthan')
    case 'up':print('uttar-pradesh')
    case 'mh':print('maharastra')
    case _ : print("wrong input !")
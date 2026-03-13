for i in range(1,6): #1  2  3  4  5
    for s in range(i-1,0,-1):
        print(" ",end="")
    for j in range(i,6):
        if i==1 or j==i or j==5:
            print("* ",end="")
        else:
            print("  ",end="")    
    print()       

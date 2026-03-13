for i in range(1,6): #1  2  3  4  5
    for s in range(i-1,0,-1):
        print("  ",end="")
    for j in range(i,6):
        print(6-i,end=" ") 
    print()       

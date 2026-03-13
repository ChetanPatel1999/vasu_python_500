for i in range(65,71): 
    for j in range(65,136-i):
            print(chr(j),end=" ")
    for s in range(65,(i*2)-66): #132-65
        print(" ",end=" ")  
    for j in range(135-i,64,-1):
        if j!=70:
            print(chr(j),end=" ")      
    print() 
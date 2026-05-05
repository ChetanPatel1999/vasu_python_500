#single threading program
import time
import threading

def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
        time.sleep(0.2)
       



t1= threading.Thread(target=table,args=[2])
t2= threading.Thread(target=table,args=[3])
t3= threading.Thread(target=table,args=[4])

t1.start()
t1.join()
t2.start()
t2.join()
t3.start()





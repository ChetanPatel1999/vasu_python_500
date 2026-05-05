#single threading program
import time
import threading

def table_2():
    for i in range(1,11):
        print(f"{2} x {i} = {2*i}")
       

def table_3():
    for i in range(1,11):
        print(f"{3} x {i} = {3*i}")
        time.sleep(0.2)

t1= threading.Thread(target=table_2)  # here t1 , t2  is a thread
t2= threading.Thread(target=table_3)

t1.start()

t2.start()
t1.join()
t2.join()
print("run program succefully")





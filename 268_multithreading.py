#single threading program
import time
def table_2():
    for i in range(1,11):
        print(f"{2} x {i} = {2*i}")
        time.sleep(0.2)

def table_3():
    for i in range(1,11):
        print(f"{3} x {i} = {3*i}")
        time.sleep(.2)


table_2()
table_3()

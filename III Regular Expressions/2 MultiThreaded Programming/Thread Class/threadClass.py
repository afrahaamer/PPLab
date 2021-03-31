import threading
import time

class MyThread(threading.Thread):
    #overriding constructor
    def __init__(self,i):
        #calling parent class constructor
        threading.Thread.__init__(self)
        self.x = i
    # defining own run method
    def run(self):
        print("Stored Value = ",self.x)
        time.sleep(4)
        print("Exiting with value",self.x)

t1 = MyThread(1)
t1.start()
t2 = MyThread(2)
t2.start()
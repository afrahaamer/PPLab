import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for x in range (7):
            print(x,"In Child")

a = MyThread()
a.start()
a.join()
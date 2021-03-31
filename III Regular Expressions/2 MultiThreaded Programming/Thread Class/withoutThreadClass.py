from threading import *

class MyThreadwtc:
    def func(self):
        for x in range(3):
            print("Child in ",x)

myT1 = MyThreadwtc()
t1 = Thread(target=myT1.func())
t1.start()
t1.join()
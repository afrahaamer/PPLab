from threading import *

print(current_thread().getName())

def tfunc():
    print("Child Thread")
child = Thread(target=tfunc())
child.start(); print('Thread Name Executing now = ',current_thread().getName())
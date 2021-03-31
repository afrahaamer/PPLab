import time
import threading
def thread1(i):
    time.sleep(3)
    print(f"i in Thread1 = {i}")

def thread2(i):
    print(f"i in Thread2 = {i}")


if __name__ == '__main__':
    t1 = threading.Thread(target=thread1,args=(10,))
    t2 = threading.Thread(target=thread2,args=(21,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
print("Execution Complete")
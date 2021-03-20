import threading 
lock =  threading.Lock()

def func1():
    for i in range(5):
        lock.acquire()
        print('acquired in func1')
        lock.release()
        
def func2():
    for i in range(5):
        lock.acquire()
        print('acquired in func2')
        lock.release()

if __name__=='__main__':
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
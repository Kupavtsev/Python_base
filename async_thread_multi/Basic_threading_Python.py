# import threading
from threading import Thread
import time

def func1_thread():
    for i in range(10000):
        print('first thread: ' + str(i))

def func2_thread():
    for i in range(10000):
        print('second thread: ' + str(i))

if __name__ == '__main__':
    start_time = time.time()
    thread1 = Thread(target = func1_thread) 
    thread2 = Thread(target = func2_thread)
    thread1.start()
    thread2.start()
    thread1.join()      # we use join to allow GIL create lock for main
    thread2.join()      # flow. Only thread1&2 will work until done
    # func1_thread()
    # func2_thread()
    end_time = time.time()
    result = end_time - start_time
    print(result)

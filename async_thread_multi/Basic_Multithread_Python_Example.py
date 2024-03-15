import threading
from threading import Thread
import time
import multiprocessing
from multiprocessing import Process

def func1_thread1():
    for i in range(10):
        time.sleep(2)
        print('user threads: ', threading.active_count()) #actual user threads at this particular time
        print(str(threading.get_native_id())+ ' ' + "first thread: "+ str(i))
        print(str(threading.main_thread())+ ' ' + "main thread: "+ str(i))

def func2_thread2():
    for i in range(10):
        time.sleep(2)
        print('user threads: ', threading.active_count())
        print(str(threading.get_native_id())+ ' ' + "second thread: "+ str(i))
        print(str(threading.main_thread())+ ' ' + "main thread: "+ str(i))
    
import concurrent.futures
def mainfunc():
    start_time = time.time()
    thread1 = Thread(target = func1_thread1)
    thread2 = Thread(target = func2_thread2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(thread1.is_alive())
    print(thread2.is_alive())

    # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    #     executor.submit(func1_thread1)
    #     executor.submit(func2_thread2)

    # func1_thread1()
    # func2_thread2()
    
    end_time = time.time()
    result = end_time - start_time
    print(result)

# if __name__ == '__main__':
#     mainfunc()


# proc1 = Process(target=func1_thread1)
#     proc1.start()
#     proc2 = Process(target=func2_thread2)
#     proc2.start()
#     proc1.join()
#     proc2.join()


import multiprocessing
from multiprocessing import Process
def print_func(continent='Asia'):
    print('The name of continent is : ', continent)
def multiprocessfunc():
    print("Number of cpu : ", multiprocessing.cpu_count())
    names = range(100)
    # names = ['America','Europe', 'Africa']
    
    procs = []
    # instantiating without any argument
    # proc = Process(target=print_func)  
    # procs.append(proc)
    # proc.start()

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()

    print("done")

if __name__ == '__main__':
    multiprocessfunc()


import os
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()
    



def foo(q):
    q.put('hello')

# if __name__ == '__main__':
#     import multiprocessing as mp
#     mp.set_start_method('spawn')
#     q = mp.Queue()
#     print(q)
#     p = mp.Process(target=foo, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()




def foo(q):
    q.put('hello')

# if __name__ == '__main__':
#     import multiprocessing as mp
#     ctx = mp.get_context('spawn')
#     q = ctx.Queue()
#     p = ctx.Process(target=foo, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()





def f(q):
    q.put([42, None, 'hello'])

# if __name__ == '__main__':
#     from multiprocessing import Process, Queue
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(q.get())    # prints "[42, None, 'hello']"
#     p.join()




def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

# if __name__ == '__main__':
#     from multiprocessing import Process, Lock
#     lock = Lock()

#     for num in range(10):
#         Process(target=f, args=(lock, num)).start()
# Without using the lock output from the different processes is liable to get all mixed up.
import threading
import time

ls = []

def count(n):
    for i in range(1,n+1):
        # print('count: ', i)
        ls.append(f'count1: {i}')
        time.sleep(0.01)
def count2(n):
    for i in range(1,n+1):
        # print('count2: ', i)
        ls.append(f'count2: {i}')
        time.sleep(0.02)


x = threading.Thread(target=count, args=(5,))
x.start()
y = threading.Thread(target=count2, args=(5,))
y.start()

x.join()
y.join()

print('Done: ' ,ls)


# def func():
#     print('func')

# t = threading.Thread(target=func)
# t.start()

# print(threading.active_count())
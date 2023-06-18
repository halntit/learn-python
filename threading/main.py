### multi-threading: 2+ threads running at the same time

# cpu-bound: threads are not useful for cpu-bound tasks (e.g. math calculation) 
# because of GIL (Global Interpreter Lock) in Python (only one thread can run at a time)
# io-bound: threads are useful for io-bound tasks (e.g. network, file, database)

# keywords: threading, thread, active_count, sleep, start, join, sequential, concurrent

import threading
import time

print(threading.active_count()) # number of threads running

def eat_breakfast():
    time.sleep(3)
    print("You finished eating breakfast")

def drink_coffee():
    time.sleep(4)
    print("You finished drinking coffee")

def study():
    time.sleep(5)
    print("You finished studying")

# sequential
# eat_breakfast()
# drink_coffee()
# study()

# concurrent
thread1 = threading.Thread(target=eat_breakfast)
thread2 = threading.Thread(target=drink_coffee)
thread3 = threading.Thread(target=study)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join() # wait for all threads to finish before continuing

print(threading.active_count()) # number of threads running
print(threading.enumerate()) # list of threads running
print(time.perf_counter()) # time in seconds


# def print_time(thread_name, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print(thread_name, time.ctime())

#     try:
#         print(thread_name, time.ctime())
#     except:
#         print("Error: unable to start thread")

# try:
#     # Create two threads as follows
#     thread1 = threading.Thread(target=print_time, args=("Thread-1", 2))
#     thread2 = threading.Thread(target=print_time, args=("Thread-2", 4))
#     thread1.start()
#     thread2.start()
# except:
#     print("Error: unable to start thread")
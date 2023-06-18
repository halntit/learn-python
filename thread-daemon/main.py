### daemon thread: a thread that runs in the background, 
# not important for program to run (e.g. garbage collector) 
# daemon threads are killed when main thread exits

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, " seconds")

    # print("Timer started")
    # time.sleep(5)
    # print("Timer ended")
x = threading.Thread(target=timer)
x.daemon = True # or threading.Thread(target=timer, daemon=True)
x.start()

answer = input("Do you wish to exit? ")
print("You entered: ", answer)

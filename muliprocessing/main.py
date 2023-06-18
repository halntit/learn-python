### multiprocessing: running tasks in parallel on different cpu cores

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    targetCount = 100000000

    print('cpu count: ', cpu_count())

    # single process (takes 7430.805506531) ??
    a = Process(target=counter, args=(targetCount,))
    a.start()
    a.join()

    # multiple processes (takes 7352.055250963) ??
    # b = Process(target=counter, args=(targetCount / 4,))
    # c = Process(target=counter, args=(targetCount / 4,))
    # d = Process(target=counter, args=(targetCount / 4,))
    # e = Process(target=counter, args=(targetCount / 4,))
    # b.start()
    # c.start()
    # d.start()
    # e.start()
    # b.join()
    # c.join()
    # d.join()
    # e.join()

    print('finished in: ', time.perf_counter(), 'seconds')

if __name__ == '__main__':
    main()
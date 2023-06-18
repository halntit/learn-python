### module time: ###
import time

print(time.ctime()) # current time
print(time.ctime(time.time())) # current time

print(time.ctime(0)) # epoch time
print(time.ctime(1)) # epoch time + 1 second

print(time.time()) # current time in epoch time

print(time.localtime()) # current time in struct_time format

# time format REF: https://docs.python.org/3/library/time.html#time.strftime
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) # current time in string format

print(time.gmtime()) # current time in struct_time format in UTC

print(time.strptime("2020-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")) # string to struct_time format

print(time.asctime()) # current time in string format (same as ctime)
time_tuple = (2023, 1, 1, 20, 0, 0, 0, 0, 0)
print(time.asctime(time_tuple)) # current time in string format
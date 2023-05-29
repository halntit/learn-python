### args: arguments for the program

def add(x, y):
    sum = x + y
    return sum
print(add(2, 3))

def add(*agrs):
    sum = 0
    # agrs[0] = 1 # agrs is a tuple and it is immutable so we can't change it
    # agrs[1] = 2 # TypeError: 'tuple' object does not support item assignment
    # cast tuple to list
    agrs = list(agrs)
    agrs[0] = 1
    for i in agrs:
        sum += i
    return sum
print(add(2, 3, 4, 5, 6, 7, 8, 9, 10))
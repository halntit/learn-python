### return statement: return a value from a function

def add(a, b):
    return a + b
print(add(1, 2))

def multiply(a, b):
    result = a * b
    return result
print(multiply(2, 3))
print(multiply(add(1, 5), 5))
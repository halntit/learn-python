### scope: the region that a variable is recognized (can be used)
# LEGB rule: Local, Enclosing, Global, Built-in

# local scope
def drink():
    drinkVar = 'water' # local variable (only available inside the function)
    return drinkVar

# print('I am drinking', drinkVar) # drinkVar is not available outside the function
print('I am drinking', drink())

# global scope
name = 'Bob' # global variable (available everywhere in the file)
print('My name is', name)

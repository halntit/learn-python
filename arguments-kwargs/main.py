### kwargs is a dictionary of keyword arguments passed to the function

def add(**kwargs):
    sum = 0
    for i in kwargs.values():
        sum += i
    return sum
print(add(a=2, b=3, c=4, d=5, e=6, f=7, g=8, h=9, i=10))

def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'], end=", ")
    print("you are " + str(kwargs['age']) + " years old")
hello(first="John", last="Doe", age=27)

def greeting(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")
    print("!")
greeting(first="John", middle="Boo", last="Doe", age=27)
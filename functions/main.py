### functions: a block of code that can be called multiple times

def helloworld():
    return "hello world"
print(helloworld())

def hello(name):
    return "hello " + name
print(hello("Bob"))
print(hello("Alice"))

def hello2(name="world"):
    return "hello " + name
print(hello2("wellington"))

def hello3(name="world", greeting="hello"):
    return greeting + " " + name
print(hello3("tom", "hi"))

def hello4(firstname, lastname, age):
    print("hello " + firstname + " " + lastname + " " + str(age))
hello4("Bob", "Smith", 25)
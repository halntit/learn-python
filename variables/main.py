### variables

# string - str
fname = "John"
print(fname)
print("Hello " + fname)
print(type(fname))

lname = "Doe"
fullName = fname + " " + lname
print(fullName)

# integer - int
age = 30
age += 1
print(age)
print(type(age))
#print("your age is: " + age)
print("your age is: " + str(age))

# float - float
height = 1.75
print(height)
print(type(height))
print("your height is: " + str(height))

# boolean - bool
isHuman = True
print(isHuman)
print(type(isHuman))
print("are you human? " + str(isHuman))

# list - list
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(type(fruits))
print(fruits[0])

# tuple - tuple
fruits = ("apple", "banana", "cherry")
print(fruits)
print(type(fruits))
print(fruits[0])

# dictionary - dict
person = {
    "fname": "John",
    "lname": "Doe",
    "age": 30,
    "height": 1.75,
    "isHuman": True
}
print(person)
print(type(person))
print(person["fname"])
print(person["lname"])
print(person["age"])
print(person["height"])
print(person["isHuman"])

# set - set
fruits = {"apple", "banana", "cherry"}
print(fruits)
print(type(fruits))
print(fruits.pop())

# frozenset - frozenset
fruits = frozenset({"apple", "banana", "cherry"})
print(fruits)
print(type(fruits))

# range - range
numbers = range(1, 6) # default first is 0
print(numbers)
print(type(numbers))
print(numbers[2])

# bytes - bytes
x = b"Hello"
print(x)
print(type(x))
print(x[0])

# bytearray - bytearray
x = bytearray(5)
print(x)
print(type(x))
print(x[0])

# memoryview - memoryview
x = memoryview(bytes(5))
print(x)
print(type(x))
print(x[0])

# complex - complex
x = 1j
print(x)
print(type(x))

# None - NoneType
x = None
print(x)
print(type(x))

# ellipsis - ellipsis
x = ...
print(x)
print(type(x))
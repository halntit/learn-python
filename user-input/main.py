name = input("what is your name? ")
age = int(input("How old are you? ")) # convert string to int
height = float(input("How tall are you? ")) # convert string to float

print("Hello " + name + "!")
print("You are " + str(age) + " years old.")
print("Next year you will be " + str(age + 1) + " years old.")
print("You are " + str(height) + "m tall.")
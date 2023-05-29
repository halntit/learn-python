### string format:
#  %s: string
#  %d: decimal
#  %f: float
#  %e: exponential
#  %E: exponential (capitalized)
#  %g: general
#  %G: general (capitalized)
#  %x: hexadecimal
#  %X: hexadecimal (capitalized)
#  %o: octal
#  %c: character
#  %r: raw
#  %%: percent sign

animal = "cow"
item = "moon"
print("The " + animal + " jumped over the " + item)

print("The %s jumped over the %s" % (animal, item))

print("The {} jumped over the {}".format(animal, item)) # positional arguments
print("The {1} jumped over the {0}".format(animal, item)) # positional arguments
# keyword arguments (named arguments) can reuse the same argument
print("The {animalKw} jumped over the {itemKw}".format(animalKw="cow", itemKw="moon"))

# f-strings
print(f"The {animal} jumped over the {item}")
print(f"The {animal.upper()} jumped over the {item.upper()}")

# format specifiers
print(f"Align this {item:10}. Nice") # 10 spaces left aligned (default)
print(f"Align this {item:>10}. Nice") # 10 spaces right aligned
print(f"Align this {item:^10}. Nice") # 10 spaces center aligned
print(f"Align this {item:*<10}. Nice") # 10 spaces left aligned with asterisks
print(f"Align this {item:*^10}. Nice") # 10 spaces center aligned with asterisks
print(f"Align this {item:*>10}. Nice") # 10 spaces right aligned with asterisks

number = 3.141592653589793
print("Pi is {:.3f}".format(number))

number = 1000000
print("The number is {:,}".format(number))

number = 125
print("The number is {:b}".format(number)) # binary

number = 127
print("The number is {:o}".format(number)) # octal

number = 64578
print("The number is {:x}".format(number)) # hexadecimal
# string methods
name = "john norman"

print(len(name)) # 11
print(name.find("o")) # 1
print(name.capitalize()) # John norman
print(name.upper()) # JOHN NORMAN
print(name.lower()) # john norman
print(name.isdigit()) # False
print(name.isalpha()) # False; True when there are no spaces
print(name.count("o")) # 2
print(name.replace("o", "a")) # john narmen

aString = "Blah"
print(aString.isalpha()) # True
print(aString*3) # BlahBlahBlah

aNumber = "4"
print(aNumber.isdigit()) # True
print(aNumber.isalpha()) # False
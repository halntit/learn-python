### index operator

name = "harry Potter"
print(name)

if (name[0] == "h"):
    print("Name starts with h")
    name = name.capitalize()
    print(name)

if (name[-1] == "r"):
    print("Name ends with r")

if name[6] == "P":
    print("Name has P at index 6")

if name[1:3] == "ar":
    print("Name has ar at index 1 and 2")

print("==========")

uName = name[0:5].upper() # upper case
print(uName)

lName = name[6:].lower() # lower case
print(lName)
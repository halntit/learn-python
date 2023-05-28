names = ['Alice', 'Joe', 'Dilbert', 'Bob', 'Jane']

# 1. List comprehensions
# 1.1. Create a new list with the first letter of each name
names1 = [name[0] for name in names]
print(names1)
# 1.2. Create a new list with the length of each name
names2 = [len(name) for name in names]
print(names2)
# 1.3. Create a new list with the names in uppercase
names3 = [name.upper() for name in names]
print(names3)
# 1.4. Create a new list with the names reversed
names4 = [name[::-1] for name in names]
print(names4)
# 1.5. Create a new list with the names sorted alphabetically
names5 = sorted(names)
print(names5)
# 1.6. Create a new list with the names sorted reverse alphabetically
names6 = sorted(names, reverse=True)
print(names6)
# 1.7. Create a new list with the names sorted by length
names7 = sorted(names, key=len)
print(names7)

print("==========")

# 2. Dictionary comprehensions
# 2.1. Create a new dictionary with the names as keys and the length of each name as values
namesDict1 = {name: len(name) for name in names}
print(namesDict1)
# 2.2. Create a new dictionary with the names as keys and the names in uppercase as values
namesDict2 = {name: name.upper() for name in names}
print(namesDict2)
# 2.3. Create a new dictionary with the names as keys and the names reversed as values
namesDict3 = {name: name[::-1] for name in names}
print(namesDict3)

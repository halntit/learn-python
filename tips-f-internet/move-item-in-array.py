fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits)

# move melon to first position
fruits.insert(0, fruits.pop(fruits.index("melon")))
print(fruits)

# move melon to last position
fruits.append(fruits.pop(fruits.index("melon")))
print(fruits)

# move melon to second position
# step by step solution
# 1. find index of melon in list
melonIndex = fruits.index("melon")
# 2. remove melon from list and store it in a variable called melon
melon = fruits.pop(melonIndex)
# 3. insert melon to second position in list (index 1)
fruits.insert(1, melon)
print(fruits)
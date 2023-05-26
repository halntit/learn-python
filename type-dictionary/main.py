### dictionary
# dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# dictionary is a key-value pair
# dictionary is mutable
# dictionary is enclosed in curly braces
# dictionary is faster than list when it comes to searching because it uses hashing

# create dictionary
capitals = {
    "India": "New Delhi",
    "USA": "Washington DC",
    "UK": "London",
    "China": "Beijing",
    "Japan": "Tokyo"
}

# print dictionary
print(capitals)

# access dictionary
print(capitals["India"])

# add item to dictionary
capitals["France"] = "Paris"
print(capitals)

# remove item from dictionary
capitals.pop("UK")
print(capitals)

# remove last item from dictionary
capitals.popitem()
print(capitals)

# access non-existent key
# print(capitals["UK"]) # KeyError: 'UK'
print(capitals.get("UK")) # None

# loop through dictionary
for key in capitals:
    print(key)

for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)

for key, value in capitals.items():
    print(key, value)

# check if key exists
if "UK" in capitals:
    print("UK exists")
else:
    print("UK does not exist")

# check if value exists
if "London" in capitals.values():
    print("London exists")

# length of dictionary
print(len(capitals))

# copy dictionary
capitals2 = capitals.copy()
print(capitals2)

# clear dictionary
capitals2.clear()
print(capitals2)

# delete dictionary
del capitals2
# print(capitals2) # NameError: name 'capitals2' is not defined

# nested dictionary
person = {
    "name": "John",
    "age": 36,
    "country": "Norway",
    "address": {
        "street": "Oslo West 16",
        "city": "Oslo",
        "state": "Oslo",
        "country": "Norway"
    }
}
print(person)

# dictionary constructor
capitals3 = dict(India="New Delhi", USA="Washington DC", UK="London")
print(capitals3)

# dictionary methods
# clear, copy, fromkeys, get, items, keys, pop, popitem, setdefault, update, values

capitals3.update({"China": "Beijing", "Japan": "Tokyo"}) # add multiple items
print(capitals3)

capitals3.update({"UK": "London updated"}) # update item
print(capitals3)
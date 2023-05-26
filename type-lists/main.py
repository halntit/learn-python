### list

# list is a collection which is ordered and changeable. Allows duplicate members.
food = ["rice", "beans", "spaghetti", "bread", "pizza"]
print(food)

# Access items
print(food[1])

# Change value
food[1] = "beans and eggs"
print(food)

# Loop through a list
for x in food:
    print(x)

# Check if item exists
if "rice" in food:
    print("Yes, 'rice' is in the food list")

# Get the length of a list
print(len(food))

# Add items
food.append("meat")
print(food)

# Add items at a specified index
food.insert(1, "fish")
print(food)

# Remove items
food.remove("fish")
print(food)

# Remove items at a specified index
food.pop(1)
print(food)

# Remove items at a specified index
del food[0]
print(food)

# Remove all items
food.clear()
print(food)

# Delete the list
del food

# Join two lists
food = ["rice", "beans", "spaghetti", "bread", "pizza"]
drinks = ["water", "juice", "soda", "wine", "beer"]
food_and_drinks = food + drinks
print(food_and_drinks)

# Join two lists using the extend() method
food.extend(drinks)
print(food)

# The list() Constructor
food = list(("rice", "beans", "spaghetti", "bread", "pizza"))
print(food)

# List Methods
# append() - Adds an element at the end of the list
# clear() - Removes all the elements from the list
# copy() - Returns a copy of the list
# count() - Returns the number of elements with the specified value
# extend() - Add the elements of a list (or any iterable), to the end of the current list
# index() - Returns the index of the first element with the specified value
# insert() - Adds an element at the specified position
# pop() - Removes the element at the specified position
# remove() - Removes the item with the specified value
# reverse() - Reverses the order of the list
# sort() - Sorts the list

food.sort()
print(food)
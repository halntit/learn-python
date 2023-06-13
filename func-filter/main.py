### filter: used with iterables and returns a new list of filtered elements.

friends = [
    ("John", 25, "M"),
    ("Jill", 17, "F"),
    ("Bob", 14, "M"),
    ("Alice", 15, "F"),
    ("Tom", 20, "M"),
    ("Mary", 25, "F"),
    ("Peter", 30, "M"),
]

print(friends)
print("=====================================")

ageLimit = lambda x: x[1] > 18
filteredFriends = filter(ageLimit, friends)
print(list(filteredFriends))
print("=====================================")
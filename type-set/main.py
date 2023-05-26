### type set in python
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets. No duplicate members.

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}

utensils.add("napkin")
print(utensils)

utensils.remove("fork")
print(utensils)

# utensils.remove("fork") # KeyError: 'fork'
utensils.discard("fork") # no error
print(utensils)

utensils.clear()
print(utensils)

utensils.update(dishes)
print(utensils)

del utensils
# print(utensils)
# NameError: name 'utensils' is not defined

utensils2 = {"fork", "spoon", "knife"}
dinner_table = utensils2.union(dishes)
print(dinner_table)

set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3, 4}

# difference
print(set1.difference(set2))
print(set2.difference(set1))

# intersection
print(set1.intersection(set2))

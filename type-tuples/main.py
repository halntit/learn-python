### tuples
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

student = ("John", 21, "male")
print(student)

print(student.count("John"))
print(student.index("male"))

for x in student:
    print(x)

if "John" in student:
    print("Yes, 'John' is in the student tuple")

print(len(student))

# assign value to tuple
# student[1] = 22
# print(student)
# TypeError: 'tuple' object does not support item assignment

# q: how to assign value to tuple in python?
# a: you can't. tuples are immutable. you can convert a tuple to a list, change the list, and convert the list back to a tuple.

del student
#print(student)
# NameError: name 'student' is not defined
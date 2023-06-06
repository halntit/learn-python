### sort() function
# It doesn't return any value, it just sort the elements in ascending order.
# It modifies the original list.
# It can't sort the list with both string and numeric values.
# It can sort the list with either string or numeric values.
# It can sort the list with both positive and negative values.
students = ['Sunny', 'Bunny', 'Chinny', 'Vinny', 'Pinny']
print(students)
print("=====================================")

# sort() function: (used with list) is used to sort the elements of the list in ascending order.
sorted_students = sorted(students)
print(sorted_students)
sorted_students = sorted(students, reverse=True)
print(sorted_students)

print("=====================================")

# sort() method: used with iterables
students.sort()
print(students)
students.sort(reverse=True)
print(students)

print("====================================================")

students = [
    {'name': 'Sunny', 'score': 90, 'age': 20},
    {'name': 'Bunny', 'score': 80, 'age': 18},
    {'name': 'Chinny', 'score': 70, 'age': 24},
    {'name': 'Vinny', 'score': 60, 'age': 21},
    {'name': 'Pinny', 'score': 50, 'age': 22}
]
print(students)
print("=====================================")

students.sort(key=lambda x: x['score'])
print(students)
students.sort(key=lambda x: x['name'])
print(students)
students.sort(key=lambda x: x['age'], reverse=True)
print(students)
### list comprehension: used with iterables and returns a new list with less syntax.

squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)
print("=====================================")

squares = [i ** 2 for i in range(1, 11)]
print(squares)
print("=====================================")

students_scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
print(students_scores)
print("=====================================")

passed_students = [i for i in students_scores if i >= 50]
print(passed_students)
print("=====================================")
 
result_students = [i if i >= 50 else "failed" for i in students_scores]
print(result_students)
print("=====================================")
 
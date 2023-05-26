### 2D lists
# A 2D list is a list that contains other lists.
# 2D lists are used to represent a matrix or a 2D array.

# Create a 2D list
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

# Access items
print(matrix[0][1])

# Change value
matrix[0][1] = 20
print(matrix)

# Loop through a 2D list
for row in matrix:
    for item in row:
        print(item)

# Check if item exists
if [1, 20, 3, 4] in matrix:
    print("Yes, [1, 20, 3, 4] is in the matrix")

# Get the number of rows
print(len(matrix))

# Get the number of columns
print(len(matrix[0]))

# Add items
matrix.append([9, 10, 11, 12])
print(matrix)

# Add items at a specified index
matrix.insert(1, [13, 14, 15, 16])
print(matrix)

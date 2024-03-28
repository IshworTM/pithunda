# Creating a 2x3 matrix (nested list)
matrix = [[1, 2, 3], [4, 5, 6]]

# Accessing elements
element = matrix[1][2]  # Returns 6

# Iterating through a matrix
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
# Outputs:
# 1 2 3
# 4 5 6

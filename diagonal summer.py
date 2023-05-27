def diagonal_sum(mat):
    n = len(mat)
    diagonal_sum = 0

    for i in range(n):
        diagonal_sum += mat[i][i]  # Add element from primary diagonal

        # Check if the element is not on the primary diagonal
        if i != n - 1 - i:
            diagonal_sum += mat[i][n - 1 - i]  # Add element from secondary diagonal

    return diagonal_sum


# Test the function
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
result = diagonal_sum(matrix)
print("Sum of diagonals:", result)

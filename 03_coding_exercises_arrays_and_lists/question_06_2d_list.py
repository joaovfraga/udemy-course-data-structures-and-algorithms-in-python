# QUESTION 06 - 2D List
#  Given 2D list calculate the sum of diagonal elements.

def diagonal_sum(matrix):
    # Initialize the sum to 0
    total = 0

    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        total += matrix[i][i]

    return total


myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(diagonal_sum(myList2D))
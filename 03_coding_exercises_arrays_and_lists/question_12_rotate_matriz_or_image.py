# Question 12 - Rotate Matrix/ Image - LeetCode 48

def rotate(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):  # Iterate over the rows
        for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
            # Swap the elements at positions (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:  # Iterate over each row in the matrix
        row.reverse()  # Reverse the elements in the current row

    print(matrix)


matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix1)

# Answer for !st question
# my answer with double for loop with O(n2) time complexity its just like brute force
def diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j :
                sum += matrix[i][j]
    return sum

# Below is optimized version of the above problem only one for loop O(n) time complexity
def diagonal_sum(matrix):
    # Initialize the sum to 0
    total = 0
    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        total += matrix[i][i]
 
    return total

# Answer for the second question (Explanation in the Q&A text file)
def diagonalSum(self, mat):
    n = len(mat)
    result = 0
    for i in range(n):
        result += mat[i][i] + mat[i][n - i - 1]
    if n % 2 == 1:
        result -= mat[n // 2][n // 2]  # // because u need to do floor division if you do normal division it give !.5 like that (we dont have 1.5 index in a list)
    return result
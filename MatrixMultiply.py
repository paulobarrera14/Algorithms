def printMatrix(m):
    for row in m:
        print(row)
def matrixMult(A, B):
    m = len(A) #rows of A
    n = len(A[0]) #columns of A
    p = len(B[0]) #columns of B
    C = [[None for i in range(p)] for j in range(m)]
    if n == len(B): #if columns of A equal rows of B
        for i in range(m):
            for j in range(p):
                sum = 0
                for k in range(n):
                    sum = sum + A[i][k] * B[k][j]
                C[i][j] = sum
    else:
        print("Cannot Multiply Matrices")
        return None
    return C

# Testing code
# Test1
A = [[ 2, -3, 3],
    [-2, 6, 5],
    [ 4, 7, 8]]
B = [[-1, 9, 1],
    [ 0, 6, 5],
    [ 3, 4, 7]]
C = matrixMult(A, B)
if not C == None:
    printMatrix(C)

# Test2
A = [[ 2, -3, 3, 0],
    [-2, 6, 5, 1],
    [ 4, 7, 8, 2]]
B = [[-1, 9, 1],
    [ 0, 6, 5],
    [ 3, 4, 7]]
C = matrixMult(A, B)
if not C == None:
    printMatrix(C)

# Test3
A = [[ 2, -3, 3, 5],
    [-2, 6, 5, -2]]
B = [[-1, 9, 1],
    [ 0, 6, 5],
    [ 3, 4, 7],
    [ 1, 2, 3]]
C = matrixMult(A, B)
if not C == None:
    printMatrix(C)
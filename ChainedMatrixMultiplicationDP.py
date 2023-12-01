def printMatrix(m):
    for row in m:
        print(row)
def chainMatrix(dims):
    # Create the empty 2-D table
    n = len(dims)-1

    m = [[0 for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n)] for j in range(n)]

    # Fill in the base case values
    for i in range(n):
        m[i][i] = 0

    # Fill in the rest of the table diagonal by diagonal
    for chainLength in range(2,n+1):
        for i in range(n+1-chainLength):
            j = i + chainLength - 1
            # Fill in m[i][j] with the best of the recursive options
            m[i][j] = float("inf")
            for k in range(i,j):
                # Two previous table values plus
                # what it cost to mult the resulting matrices
                q = m[i][k]+m[k+1][j]+dims[i]*dims[k+1]*dims[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k # Records optimal split position
    printMatrix(m)
    return m[0][n-1], parenStr(s, 0, n-1)

def parenStr(s, i, j):
    if i == j:
        return "A" + str(i)
    else:
        return "(" + parenStr(s, i, s[i][j]) + ")(" + parenStr(s, s[i][j] + 1, j) + ")"

dims = [30,35,15,5,10,20,25]
cost, result = chainMatrix(dims)
print(result)
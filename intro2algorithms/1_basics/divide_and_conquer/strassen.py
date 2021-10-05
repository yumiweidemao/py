"""
Strassen algorithm is used for matrix multiplication.
Its time complexity is reduced to O(n**lg(7)), namely O(n**2.81), which is less than O(n**3) of 
the regular algorithm.
"""

# This is a regular matrix mult. function
def square_matrix_multiply(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Function that prints a matrix
def print_matrix(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            print(A[i][j], end=" ")
        print("\n")

"""
Let A, B be square matrices whose width is a power of 2, then A, B can be
divided into 4 smaller square matrices:
    A = [[A1, A2],        B = [[B1, B2],
         [A3, A4]]             [B3, B4]]

Let C = AB, C can also be divided into 4 smaller square matrices:
    C = [[C1, C2],
         [C3, C4]]

C1 = A1B1 + A2B3
C2 = A1B2 + A2B4
C3 = A3B1 + A3B3
C4 = A3B2 + A4B4

Base case: when A, B are 1*1 matrices, C = C1 = A1*B1
then 8 matrix multiplications are needed:
    T(n) = 8T(n/2) + O(n**2)
Time complexity = O(n**(lg(8))) = O(n**3).

Strassen algorithm calculates only 7 matrix multiplications:
    T(n) = 7T(n/2) + O(n**2)
Reaching a time complexity of O(n**2.81).

First, matrix add/subtract functions should be defined.
"""

def matrix_add(A, B):
    # matrix add, time complexity = O(n**2)
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def matrix_subtract(A, B):
    # matrix subtract, time complexity = O(n**2)
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def divide_matrix(A):
    """
    divide an n*n matrix into 4 sub-matrices.
    """
    n = len(A) # n must be power of 2
    mid = n // 2

    A11 = [[0 for _ in range(mid)] for _ in range(mid)]
    A12 = [[0 for _ in range(mid)] for _ in range(mid)]
    A21 = [[0 for _ in range(mid)] for _ in range(mid)]
    A22 = [[0 for _ in range(mid)] for _ in range(mid)]

    for i in range(n):
        for j in range(n):
            if i < mid and j < mid:
                A11[i%mid][j%mid] = A[i][j]
            elif i >= mid and j >= mid:
                A22[i%mid][j%mid] = A[i][j]
            elif i < mid and j >= mid:
                A12[i%mid][j%mid] = A[i][j]
            elif i >= mid and j < mid:
                A21[i%mid][j%mid] = A[i][j]

    return (A11, A12, A21, A22)

def merge_matrix(C11, C12, C21, C22):
    # merge 4 n*n matrices into a 2n*2n matrix
    mid = len(C11)
    n = mid * 2

    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i < mid and j < mid:
                C[i][j] = C11[i%mid][j%mid]
            elif i >= mid and j >= mid:
                C[i][j] = C22[i%mid][j%mid]
            elif i < mid and j >= mid:
                C[i][j] = C12[i%mid][j%mid]
            elif i >= mid and j < mid:
                C[i][j] = C21[i%mid][j%mid]

    return C

def strassen(A, B):
    """
    A, B must be n*n matrices, n must be a power of 2. If not, fill A & B with
    zeros so that n is a power of 2.

    returns a matrix C, C = AB, time complexity = O(n**2.81).
    """
    n = len(A)

    # Base case: only 1 element, C11 = A11*B11
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # divide matrices
    A11, A12, A21, A22 = divide_matrix(A)
    B11, B12, B21, B22 = divide_matrix(B)

    # Initialize matrices for strassen algorithm
    S1 = matrix_subtract(B12, B22)  # S1 = B12 - B22
    S2 = matrix_add(A11, A12)       # S2 = A11 + A12
    S3 = matrix_add(A21, A22)       # S3 = A21 + A22
    S4 = matrix_subtract(B21, B11)  # S4 = B21 - B11
    S5 = matrix_add(A11, A22)       # S5 = A11 + A22
    S6 = matrix_add(B11, B22)       # S6 = B11 + B22
    S7 = matrix_subtract(A12, A22)  # S7 = A12 - A22
    S8 = matrix_add(B21, B22)       # S8 = B21 + B22
    S9 = matrix_subtract(A11, A21)  # S9 = A11 - A21
    S10 = matrix_add(B11, B12)      # S10 = B11 + B12

    # recursively calculate 7 matrices using Aij, Bij and the 10 matrices above
    P1 = strassen(A11, S1)          # P1 = A11 * S1 = A11*B12 - A11*B22
    P2 = strassen(S2, B22)          # P2 = S2 * B22 = A11*B22 + A12*B22
    P3 = strassen(S3, B11)          # P3 = S3 * B11 = A21*B11 + A22*B11
    P4 = strassen(A22, S4)          # P4 = A22 * S4 = A22*B21 - A22*B11
    P5 = strassen(S5, S6)           # P5 = S5 * S6 = A11*B11 + A11*B22 + A22*B11 + A22*B22
    P6 = strassen(S7, S8)           # P6 = S7 * S8 = A12*B21 + A12*B22 - A22*B21 - A22*B22
    P7 = strassen(S9, S10)          # P7 = S9 * S10 = A11*B11 + A11*B12 - A21*B11 - A21*B12

    # calculate C11, C12, C21, C22

    # C11 = P5 + P4 - P2 + P6
    C11 = matrix_subtract(matrix_add(P5, P4), matrix_subtract(P2, P6))
    # C12 = P1 + P2
    C12 = matrix_add(P1, P2)
    # C21 = P3 + P4
    C21 = matrix_add(P3, P4)
    # C22 = P5 + P1 - P3 - P7
    C22 = matrix_subtract(matrix_add(P5, P1), matrix_add(P3, P7))

    # merge matrices
    C = merge_matrix(C11, C12, C21, C22)

    return C

# testing with two matrices

A = [[1, 4, 2, 6],
     [4, 8, -1, 5],
     [9, 1, 3, 3],
     [0, 1, 2, 5]]

B = [[4, 3, 1, 0],
     [2, 8, 7, 9],
     [5, -1, 0, -3],
     [1, 5, 3, 2]]

S = strassen(A, B)
C = square_matrix_multiply(A, B)

if S == C:
    print("Strassen algo succeeded.")

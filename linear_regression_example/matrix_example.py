from typing import List
from typing import Tuple


Matrix = List[List[float]]
print(Matrix)

Vector = List[float]

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [5, 6]]

for i in A:
    print("{0}".format(i))
    
    for j in i:
        print("{0}".format(j))    
    print("")

print("==================================")

for i in B:
    print("{0}".format(i))
    
    for j in i:
        print("{0}".format(j))
    print("")


def shape(A: Matrix) -> Tuple[int: int]:
    """Return (Number of Rows, Number of Columns)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    
    return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)


def get_row(A: Matrix, i: int) -> Vector:
    """Return number `i` of `A`s row"""
    return A[i]


# True Case
print(get_row(A, 1) == [4, 5, 6])

# False Case
print(get_row(A, 1) == [1, 2, 3])


def get_column(A: Matrix, j: int) -> Vector:
    """Return number `j` of `A`s column"""
    return [A_i[j]
            for A_i in A]
    
# True Case
print(get_column(B, 1) == [2, 4, 6])
print(get_column(B, 0) == [1, 3, 5])

# False Case
print(get_column(B, 1) == [1, 2, 3])
print(get_column(B, 0) == [2, 4, 6])

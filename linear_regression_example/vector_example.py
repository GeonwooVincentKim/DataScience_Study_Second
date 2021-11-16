from typing import List

Vector = List[float]
print(Vector)

height_weight_age = [70, # Inch,
                     170, # Pount,
                     40] # Age

for i in height_weight_age:
    print(i)
    
print("----------------------------")

grades = [95, # Test 1 Score
          80, # Test 2 Score,
          75, # Test 3 Score,
          62] # Test 4 Score

for i in grades:
    print(i)
    
print("---------------------------------------")

def add(v: Vector, w: Vector) -> Vector:
    """Plus Each Elements"""
    assert len(v) == len(w), "vectors must be the same length"
    
    return [v_i + w_i for v_i, w_i in zip(v, w)]


# assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
print("Add is True?? -> {0}".format(add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]))


def subtract(v: Vector, w: Vector) -> Vector:
    """Extract Each elements"""
    assert len(v) == len(w), "vectors must be the same length"
    
    return [v_i - w_i for v_i, w_i in zip(v, w)]


# assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
print("Subtract is True?? -> {0}".format(subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]))


def vector_sum(vectors: List[Vector]) -> Vector:
    """Add each elements of Every Vector """
    assert vectors, "no vectors provided!"
    
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"
    
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]


# assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
print("Vector-Sum is True?? -> {0}".format(vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]))


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiply Every elements with `c`"""
    return [c * v_i for v_i in v]


# assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]
print("Scalar-Multiply is True?? -> {0}".format(scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]))

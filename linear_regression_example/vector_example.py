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
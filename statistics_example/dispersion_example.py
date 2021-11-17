import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from typing import List
from scratch.linear_algebra import sum_of_squares
from friendcount_histogram import num_friends


def data_range(xs: List[float]):
    return max(xs) - min(xs)


print(data_range(num_friends) == 99)

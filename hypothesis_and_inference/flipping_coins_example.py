from typing import Tuple
import math


def normal_approximation_to_binomial(n: int, p: float):
    """
        Calculate mu(average) and sigma(Standard Deviation) 
        that goes for `Binomial(n, p)` function
    """

    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    print(sigma)

    return mu, sigma


print("{0}".format(normal_approximation_to_binomial(1000, 0.5)))

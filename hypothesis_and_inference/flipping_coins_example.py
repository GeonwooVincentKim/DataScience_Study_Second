import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.join(os.path.dirname(__file__)))))

from typing import Tuple
import math

from statistics_example.continuous_distribution_example import normal_cdf

normal_probability_below = normal_cdf


def normal_approximation_to_binomial(n: int, p: float):
    """
        Calculate mu(average) and sigma(Standard Deviation) 
        that goes for `Binomial(n, p)` function
    """

    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    print(sigma)

    return mu, sigma


def normal_probability_above(lo: float, mu: float=0, sigma: float=1):
    """
    Cumulative Distribution Function represents the probability 
    that the Random-Variable smaller than some particular value 
    """
    return 1 - normal_cdf(lo, mu, sigma)


def normal_probability_between(lo: float, hi: float, mu: float=0, sigma: float=1):
    """
    Probability the normal-distribution that follows `mu(average)` and `sigma(standard-deviation)`
    exists between `lo` and `hi`
    """
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


print("\n---------------------\n")
print("Normal Approximation to binomial function -> {0}".format(normal_approximation_to_binomial(1000, 0.5)))
print("Normal Probability Above -> {0}".format(normal_probability_above(0.95, 1000, 0.5)))

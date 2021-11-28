import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.join(os.path.dirname(__file__)))))

from typing import Tuple
import math
import random
from matplotlib import pyplot as plt

from statistics_example.continuous_distribution_example import inverse_normal_cdf, normal_cdf

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


def normal_probabilty_outside(lo: float, hi: float, mu: float=0, sigma: float=1):
    """
       The probability that the Normal-Distribution that follows 
       "mu(average)" and "sigma(standard-deviation) not existing between them."
    """
    return 1 - normal_probability_between(lo, hi, mu, sigma)


def normal_upper_bound(probability: float, mu: float=0, sigma: float=1):
    """
        Return `z` value, P(Z <= z) = probability
    """
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability: float, mu: float=0, sigma: float=1):
    """
        Return `z` value, P(Z >= z) = probability
    """
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability: float, mu:float = 0, sigma: float=1):
    """
        Include input probability value, and
        returns a Symmetrical-Interval around the mean(average)
    """
    tail_probability = (1 - probability) / 2
    
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    print("Upper Bound Value -> {0}\nLower Bound Value -> {1}".format(upper_bound, lower_bound))

    return lower_bound, upper_bound


print("\n---------------------\n")
# Flip the coins 1000 times and the average equals to 500 (1000 * 0.5 = 500)
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
print("Mu_0 -> {0}\nsigma_0 -> {1}".format(mu_0, sigma_0))

# p = 0.5, and the interval of `significance-level` are 5%. 
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
print("LO -> {0}\nHI -> {1}".format(lo, hi))

# (469, 531)
lower_bound, upper_bound = normal_two_sided_bounds(0.95, mu_0, sigma_0)
print("Lower Bound -> {0}\nUpper-Bound -> {1}".format(lower_bound, upper_bound))

# p = 0.5, and the interval of `significance-level` are 5%.
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
print("LO -> {0}\nHI -> {1}".format(lo, hi))

# Standard Deviation and Actual-Mean when the `p = 0.55`
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
print("Mu_1 -> {0}\nsigma_1 -> {1}".format(mu_1, sigma_1))

type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability
print("Type 2 Probability -> {0}\nPower -> {1}".format(type_2_probability, power))

plt.scatter(lower_bound, upper_bound)
plt.show()


def two_sided_p_value(x: float, mu: float=0, sigma: float=1):
    """
        What is the Probability of Extreme-Value like `x` from a 
        `normal-distribution` that follows `mu(eval)` and `sigma(standard-deviation)`?
    """
    if x >= mu:
        return 2 * normal_probability_above(x, mu, sigma)    
    else:
        return 2 * normal_probability_below(x, mu, sigma)


two_sided_p_value(529.5, mu_0, sigma_0)
print("Two-Sided P-Value -> {0}".format(two_sided_p_value(529.5, mu_0, sigma_0)))
print("Normal Probability Between (Natural-Number) -> {0}".format(normal_probability_between(530, 531, mu_0, sigma_0)))
print("Normal Probability Between -> {0}".format(normal_probability_between(529.5, 530.5, mu_0, sigma_0)))

plt.bar(mu_0, sigma_0)
plt.show()


extreme_value_count = 0
for _ in range(1000):
    num_heads = sum(1 if random.random() < 0.5 else 0
                    for _ in range(1000))
    
    if num_heads >= 530 or num_heads <= 470:
        extreme_value_count += 1
    
print(59 < extreme_value_count < 65, f"{extreme_value_count}")
print("Two Sided value (after compare extreme-value-count) -> {0}".format(two_sided_p_value(531.5, mu_0, sigma_0)))

upper_p_value = normal_probability_above
lower_p_value = normal_probability_below

print("Upper `P` Value -> {0}".format(upper_p_value(524.5, mu_0, sigma_0)))  # 0.061
print("Upper `P` Value -> {0}".format(upper_p_value(526.5, mu_0, sigma_0)))  # 0.047


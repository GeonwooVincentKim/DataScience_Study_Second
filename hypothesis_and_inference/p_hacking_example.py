from typing import List
import random
import math

import os
import sys

from flipping_coins_example import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))



def run_experiment():
    return [random.random() < 0.5 for _ in range(1000)]


def reject_fairness(experiment: List[bool]):
    num_heads = len([filp for filp in experiment if filp])
    return num_heads < 469 or num_heads > 531


random.seed(0)
experiments = [run_experiment() for _ in range(1000)]

num_rejections = len([
    experiment
    for experiment in experiments
    if reject_fairness(experiment)
])

print("Num Rejections -> {0}".format(num_rejections == 46))


def estimated_parameters(N: int, n: int):
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    
    return p, sigma


def a_b_test_statistic(N_A: int, n_A: int, N_B: int, n_B: int):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    print(p_A, sigma_A)
    
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    print(p_B, sigma_B)
    
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)


z = a_b_test_statistic(1000, 200, 1000, 150)
print("A/B Test Statistics -> {0}".format(z))
print("{0}".format(two_sided_p_value(z)))


def B(alpha: float, beta: float):
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)


def beta_pdf(x: float, alpha: float, beta: float):
    if x <= 0 or x >= 1:
        return 0
    
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)

import math
from matplotlib import pyplot as plt

SQRT_TWO_PI = math.sqrt(2 * math.pi)


def uniform_pdf(x: float):
    return 1 if 0 <= x < 1 else 0


def uniform_cdf(x: float):
    if x < 0: return 0
    elif x < 1: return x
    else : return 1


# Normal Distribution 
def normal_pdf(x: float, mu: float = 0, sigma: float = 1):
    return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))


xs = [x / 10.0 for x in range(-50, 50)]
print(xs)

plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
plt.plot(xs, [normal_pdf(x, mu=1) for x in xs], '.-', label='mu=1, sigma=1')

plt.legend()
plt.title("Various Normal PDFs")
plt.show()


# Cumulative Distribution Function
def normal_cdf(x:float, mu:float = 0, sigma: float = 1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
plt.plot(xs, [normal_cdf(x, mu=1) for x in xs], '.-', label='mu=1, sigma=1')

plt.plot(xs, [normal_cdf(x, mu=-1, sigma=-1) for x in xs], '^', label='mu=-1, sigma=-1')
plt.plot(xs, [normal_cdf(x, sigma=-1) for x in xs], '*', label='mu=1, sigma=-1')

plt.legend(loc=4)
plt.title("Various Normal CDFs")
plt.show()

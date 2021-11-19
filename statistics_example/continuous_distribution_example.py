from matplotlib import pyplot as plt


def uniform_pdf(x: float):
    return 1 if 0 <= x < 1 else 0


plt.plot(uniform_pdf(23), uniform_pdf(23))
plt.show()

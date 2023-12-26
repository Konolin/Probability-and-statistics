import matplotlib.pyplot as plt
from scipy.stats import norm, expon
import numpy as np


def ex1():
    # a
    mu = 199
    sigma = 3
    n = 10000
    data = norm.rvs(mu, sigma, n)
    average = np.mean(data)
    print("Average:", average)

    # b
    print(f"Probability to have less than 195 g: {sum(data <= 195) / n}")
    print(f"Probability to have between 195 and 198 g: {np.mean((data >= 195) * (data <= 198)) / n}")
    print(f"Probability to have more than 195 g: {sum(data > 195) / n}")

    # c
    hfg, klasse = np.histogram(data, bins=16)
    print(f"Haufingkeit: {hfg}")
    print(f"Klasse: {klasse}")

    plt.hist(data, bins=16, density=True, edgecolor="black", label="rel. Hfg.")
    x = np.linspace(min(data), max(data), 100)
    pdf_values = norm.pdf(x, mu, sigma)
    plt.plot(x, pdf_values)
    plt.show()


def ex2():
    n = 1000
    alpha = 1 / 12
    data = expon.rvs(loc=0, scale=1 / alpha, size=n)

    # a
    mean = np.mean(data)
    print("Mean is: ", mean)

    # b
    hfg, klassen = np.histogram(data, bins=12)
    for i in range(len(hfg)):
        print(f"Klasse {i + 1:2d}: {hfg[i]:3d} Daten, [{klassen[i]:8.4f}, {klassen[i + 1]:8.4f}]")

    plt.hist(data, bins=12, density=True, edgecolor="black", label="rel. Hfg.")
    plt.show()

    x = np.linspace(min(data) - 2, max(data) + 2, 100)
    y = expon.pdf(x, loc=0, scale=1 / alpha)

    plt.plot(x, y, 'r-')
    plt.show()



def main():
    # ex1()
    ex2()


if __name__ == "__main__":
    main()

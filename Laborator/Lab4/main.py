import math

import numpy
from scipy.stats import binom
from matplotlib.pyplot import bar, show, hist, grid, legend, xticks


def ex1():
    n = 1000
    x = [0, 1, 3, 5]
    p = [0.4, 0.1, 0.3, 0.2]
    rng = numpy.random.default_rng()
    data = rng.choice(x, size=n, replace=True, p=p)
    results, count = numpy.unique(data, return_counts=True)
    bar(results, count / n, width=0.9, color="red", edgecolor="black", alpha=0.4, label="Relative probability")
    bar(x, p, width=0.7, color="blue", edgecolor="black", alpha=0.5, label="Theoretical probability")
    legend(loc="lower left")
    xticks(range(min(x), max(x) + 1))
    grid()
    show()


def ex2():
    simulations = 1000
    errors = [0, 1, 2, 3, 4]
    probability = [0.25, 0.35, 0.25, 0.10, 0.05]
    rng = numpy.random.default_rng()
    data = rng.choice(errors, size=simulations, replace=True, p=probability)
    values, count = numpy.unique(data, return_counts=True)
    print(f"Probability of max 1 error: {(count[0] + count[1]) / simulations}")
    print(f"Average error count: {numpy.mean(data)}")
    print(f"Theoretical average error count: {sum(x * p for x, p in zip(errors, probability))}")


def ex3():
    N = 1000
    max_value = 8
    probability = 0.5
    all_values = []

    for i in range(max_value + 1):
        all_values.append(i)

    X = binom.rvs(max_value, probability, size=N)
    w = binom.pmf(all_values, max_value, probability)

    bar(all_values, w, width=0.9, color="red", edgecolor="black", label="Theor. Haufigkeiten ")
    xticks(range(0, max_value + 1))

    xx, count = numpy.unique(X, return_counts=True)
    bar(xx, count / N, width=0.6, color="blue", edgecolor="black", label="Rel. Haufigkeiten ")

    legend(loc="upper right")

    grid()
    show()


def ex4():
    simulations = 1000
    nr_computers = 7
    probability = 0.4

    values_sim = binom.rvs(nr_computers, probability, size=simulations)
    count = 0
    for value in values_sim:
        if value <= 3:
            count += 1
    print(f"Max 3 computers (simulation): {count / simulations}")



def main():
    # ex1()
    # ex2()
    # ex3()
    ex4()


if __name__ == "__main__":
    main()

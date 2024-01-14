import matplotlib.pyplot as plt
import numpy as np


def main():
    num_data = 2000
    val = [-1, 0, 1, 2]
    prob = [0.25, 0.25, 0.25, 0.25]

    # a)
    rng = np.random.default_rng()
    x = rng.choice(val, size=num_data, replace=True, p=prob)
    y = rng.choice(val, size=num_data, replace=True, p=prob)

    z = x + y
    values, counts = np.unique(z, return_counts=True)
    for i in range(len(values)):
        print(f"X + Y = {values[i]} hat relative Hfg. = {counts[i] / num_data}")
    print()

    # b)
    plt.hist(z, bins=np.arange(min(z) - 0.5, max(z) + 1.5, 1), density=True, edgecolor='black', alpha=0.7)
    plt.xlabel("X + Y")
    plt.ylabel("Relative Frequency")
    plt.xticks(np.arange(min(z), max(z) + 1, 1))
    plt.title("Histogram of X + Y")
    plt.show()

    # c)
    print(f"P(X + Y < 1) = {np.sum(z < 1) / num_data}\n")

    # d)
    print(f"Theor. P(X + Y = -2) = {0.25 ** 2}")  # -1 + -1
    print(f"Theor. P(X + Y = -1) = {2 * 0.25 ** 2}")  # -1 + 0; 0 + -1
    print(f"Theor. P(X + Y = 0) = {3 * 0.25 ** 2}")  # 0 + 0; 1 + -1; -1 + 1
    print(f"Theor. P(X + Y = 1) = {4 * 0.25 ** 2}")  # -1 + 2; 2 + -1; 1 + 0; 0 + 1
    print(f"Theor. P(X + Y = 2) = {3 * 0.25 ** 2}")  # 0 + 2; 2 + 0; 1 + 1
    print(f"Theor. P(X + Y = 3) = {2 * 0.25 ** 2}")  # 2 + 1; 1 + 2
    print(f"Theor. P(X + Y = 4) = {0.25 ** 2}\n")  # 2 + 2

    # e)
    print(f"Theor. P(X + Y < 1) = {0.25 ** 2 + 2 * 0.25 ** 2 + 3 * 0.25 ** 2}")


if __name__ == '__main__':
    main()

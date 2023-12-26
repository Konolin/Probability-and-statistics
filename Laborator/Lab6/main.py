import random
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import expon, uniform


def ex1():
    n = 800
    x = [4, 5, 6, 7, 8, 9, 10]
    p = [0.05, 0.1, 0.1, 0.35, 0.2, 0.1, 0.1]

    d = random.choices(x, weights=p, k=n)

    # Calculate the expected value
    expected_value = np.mean(d)
    print("Expected value E(X):", expected_value)

    # Theoretical Expected value E(X)
    expected_value = sum(x * p for x, p in zip(x, p))
    print("Theoretical Expected value E(X):", expected_value)

    # Calculate the variance
    variance = np.var(d)
    print("Variance V(X):", variance)

    # Theoretical Variance V(X)
    expected_value_squared = sum(x ** 2 * p for x, p in zip(x, p))
    variance = expected_value_squared - expected_value ** 2
    print("Theoretical Variance V(X):", variance)

    # Calculate the probability P(X ≤ 7)
    prob_x_leq_7 = sum(1 for d in d if d <= 7) / n
    print("P(X ≤ 7):", prob_x_leq_7)

    # Theoretical Probability P(X ≤ 7)
    prob_x_leq_7 = sum(p for x, p in zip(x, p) if x <= 7)
    print("Theoretical P(X ≤ 7):", prob_x_leq_7)

    # Calculate the probability P(X > 4)
    prob_x_gt_4 = sum(1 for d in d if d > 4) / n
    print("P(X > 4):", prob_x_gt_4)

    # Theoretical Probability P(X > 4)
    prob_x_gt_4 = sum(p for x, p in zip(x, p) if x > 4)
    print("Theoretical P(X > 4):", prob_x_gt_4)

    plt.subplot(1, 2, 1)
    plt.hist(d, bins=len(x), density=True, edgecolor='black')
    plt.title('Relativen Häufigkeiten')
    plt.xlabel('Werte')
    plt.ylabel('Relative Häufigkeit')

    # Absolute Häufigkeiten
    plt.subplot(1, 2, 2)
    plt.hist(d, bins=len(x), density=False, edgecolor='black', color='r')
    plt.title('Absoluten Häufigkeiten')
    plt.xlabel('Werte')
    plt.ylabel('Absolute Häufigkeit')

    plt.tight_layout()
    plt.show()


def ex2():
    n = 1000
    x_min = y_min = z_min = -2
    x_max = y_max = z_max = 2
    target_point = (2, 2, 2)

    # a
    points = [(random.uniform(x_min, x_max), random.uniform(y_min, y_max), random.uniform(z_min, z_max)) for _ in
              range(n)]
    distances = [math.dist(point, target_point) for point in points]
    expected_value_x = sum(distances) / n
    print("Estimation of the expected value of X: ", expected_value_x)

    # b
    center = (0, 0, 0)
    distances = [math.dist(point, center) for point in points]
    inside_points = 0
    for distance in distances:
        if distance <= 2:
            inside_points += 1
    probability = inside_points / n
    print("Probability of a point being inside the sphere: ", probability)

    theoretical_probability = (4 / 3 * math.pi * 8) / 64
    print("Theoretical probability", theoretical_probability)


def ex3():
    prob_D1 = 0.4
    prob_D2 = 0.6

    printing_time_D1 = expon(scale=1 / 5)
    printing_time_D2 = uniform(loc=4, scale=2)

    n = 10000
    print_times = np.zeros(n)

    for i in range(n):
        chosen_printer = np.random.choice(['D1', 'D2'], p=[prob_D1, prob_D2])

        if chosen_printer == 'D1':
            print_times[i] = printing_time_D1.rvs()
        else:
            print_times[i] = printing_time_D2.rvs()

    probability_more_than_5_seconds = np.mean(print_times > 5)

    mean_printing_time = np.mean(print_times)
    std_printing_time = np.std(print_times)

    print(f"a) Estimated probability of printing taking more than 5 seconds: {probability_more_than_5_seconds:.4f}")
    print(f"b) Estimated mean printing time: {mean_printing_time:.2f} seconds")
    print(f"   Estimated standard deviation of printing time: {std_printing_time:.2f} seconds")


def ex4():
    print()


def main():
    # ex1()
    # ex2()
    # ex3()
    ex4()


if __name__ == "__main__":
    main()

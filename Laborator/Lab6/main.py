import math
import random
from itertools import product

import matplotlib.pyplot as plt
import numpy as np
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
    # Sei die Gleichung zweiten Grades x^2 + Bx + C = 0, wobei B, C ∼ Unif[−1, 1] unabhangige ZG sind.
    # Anzahl der Simulationen
    num_simulations = 10000

    # Zufallsvariablen B und C
    B_values = uniform.rvs(loc=-1, scale=2, size=num_simulations)
    C_values = uniform.rvs(loc=-1, scale=2, size=num_simulations)

    # a) die Wahrscheinlichkeit, dass beide Wurzeln der Gleichung reell sind;
    real_roots = []
    for i in range(num_simulations):
        if B_values[i] ** 2 - 4 * C_values[i] >= 0:
            real_roots.append(
                (((-B_values[i] + np.sqrt(B_values[i] ** 2 - 4 * C_values[i])) / 2),
                 ((-B_values[i] - np.sqrt(B_values[i] ** 2 - 4 * C_values[i])) / 2))
            )
    prob_real_roots = len(real_roots) / num_simulations
    print(f"a) Wahrscheinlichkeit, dass beide Wurzeln reell sind: {prob_real_roots:.4f}")

    # b) die Wahrscheinlichkeit, dass beide Wurzeln der Gleichung positiv sind;
    num_pos_roots = 0
    for i in range(len(real_roots)):
        if real_roots[i][0] >= 0 and real_roots[i][1] >= 0:
            num_pos_roots += 1
    prob_positive_roots = num_pos_roots / num_simulations
    print(f"b) Wahrscheinlichkeit, dass beide Wurzeln positiv sind: {prob_positive_roots:.4f}")

    # c) den Erwartungswert und die Varianz der Summe der beiden Wurzeln.
    sum_roots = []
    for i in range(len(real_roots)):
        sum_roots.append(real_roots[i][0] + real_roots[i][1])
    expected_value = np.mean(sum_roots)
    variance = np.var(sum_roots)
    print(f"c) Erwartungswert der Summe der Wurzeln: {expected_value:.4f}")
    print(f"   Varianz der Summe der Wurzeln: {variance:.4f}")


def ex5():
    # In einer Urne sind 20 rote Kugeln, 15 blaue Kugeln, 5 grune Kugeln und 10 schwarze Kugeln. Man
    # simuliere N(= 200, 1000, . . .) Ziehungen mit Zurucklegen und zeige (print) die relative Haufigkeit an mit
    # welcher jede Farbe auftaucht. Man vergleiche die theoretischen Resultate mit den Ergebnissen aus den
    # Simulationen. Man gebe die Ergebnisse der ersten 10 Ziehungen an!
    n = 1000
    count_red = 0
    count_green = 0
    count_blue = 0
    count_black = 0
    for _ in range(n):
        urn = np.array(['red'] * 20 + ['blue'] * 15 + ['green'] * 5 + ['black'] * 10)
        draws = np.random.choice(urn, size=10, replace=True)
        for draw in draws:
            if draw == 'red':
                count_red += 1
            elif draw == 'blue':
                count_blue += 1
            elif draw == 'green':
                count_green += 1
            else:
                count_black += 1

    print(f"P(rot) = {count_red / (n * 10)}")
    print(f"P(blau) = {count_blue / (n * 10)}")
    print(f"P(grun) = {count_green / (n * 10)}")
    print(f"P(schwarz) = {count_black / (n * 10)}")

    total_balls = 20 + 15 + 5 + 10
    prob_red = 20 / total_balls
    prob_blue = 15 / total_balls
    prob_green = 5 / total_balls
    prob_black = 10 / total_balls
    print(f"Theoretische Wahrscheinlichkeiten:")
    print(f"P(rot) = {prob_red}")
    print(f"P(blau) = {prob_blue}")
    print(f"P(grun) = {prob_green}")
    print(f"P(schwarz) = {prob_black}")


def ex6():
    # Eine Urne enthalt 10 Kugeln mit der Ziffer 0, 20 Kugeln mit der Ziffer 1, 20 Kugeln mit der Ziffer 2.
    # Aus der Urne werden 3 Kugeln ohne Zurucklegen gezogen. X sei das Produkt der 3 erhaltenen Zahlen.
    # Man schatze anhand Simulationen den Erwartungswert und die Varianz von X!
    # Man erstelle anhand Simulationen das Histogramm der absoluten Haufigkeiten fur die Werte von X!
    # In ein zweites Bild zeichne man ein zweites Histogramm mit den (theoretischen) Wahrscheinlichkeiten der ZG X.
    n = 10000
    urne = [0, 1, 2]
    counts = [10, 20, 20]
    simulated_values = []
    for _ in range(n):
        draws = random.sample(urne, counts=counts, k=3)
        product_value = np.prod(draws)
        simulated_values.append(product_value)

    # Berechne Erwartungswert und Varianz
    mean_value = np.mean(simulated_values)
    variance_value = np.var(simulated_values)
    print(f"Erwartungswert von X: {mean_value}")
    print(f"Varianz von X: {variance_value}")

    # Histogramm der absoluten Häufigkeiten
    plt.hist(simulated_values, bins=np.arange(min(simulated_values), max(simulated_values) + 2) - 0.5, density=False,
             edgecolor="black", label="absolute Hfg.")
    plt.title('Histogramm der absoluten Haufigkeiten')
    plt.xlabel('X')
    plt.ylabel('Absolute Haufigkeit')
    plt.show()

    # Histogramm mit theoretischen Wahrscheinlichkeiten
    all_possible_outcomes = list(product(urne, repeat=3))
    theoretical_probabilities = [counts[0] / sum(counts) * counts[1] / sum(counts) * counts[2] / sum(counts) for _ in
                                 all_possible_outcomes]

    plt.hist(simulated_values, bins=np.arange(min(simulated_values), max(simulated_values) + 2) - 0.5, density=True,
             edgecolor="black", label="relative Hfg.")
    # plt.plot(theoretical_probabilities, bins=np.arange(min(simulated_values), max(simulated_values) + 2) - 0.5,
    #          density=True, label="theoretische Wahrscheinlichkeiten")
    plt.title('Histogramm mit theoretischen Wahrscheinlichkeiten')
    plt.xlabel('X')
    plt.ylabel('Relative Haufigkeit')
    plt.legend()
    plt.show()


def main():
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    ex6()


if __name__ == "__main__":
    main()

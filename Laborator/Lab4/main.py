import numpy
from matplotlib.pyplot import grid, xticks, show, ylabel, xlabel, title, hist, bar, legend
from numpy import random, argmax, array, mean, arange
from scipy.stats import binom


def ex1():
    # Generieren von zufalligen Werten der ZG: X ∼ /0   1   3   5  \
    #                                              \0.4 0.1 0.3 0.2/
    # Simulation von zufalligen Werten fur X in Python:
    n = 1000
    x = [0, 1, 3, 5]
    p = [0.4, 0.1, 0.3, 0.2]
    rng = numpy.random.default_rng()
    data = rng.choice(x, size=n, replace=True, p=p)
    results, count = numpy.unique(data, return_counts=True)

    # Man erstelle das Histogramm der relativen Haufigkeiten fur 1000 zufallige Werte von X. Auf demselben Bild
    # zeichne man auch die Balken fur die theoretischen Wahrscheinlichkeiten.
    bar(results, count / n, width=0.9, color="red", edgecolor="black", alpha=0.4, label="Relative probability")
    bar(x, p, width=0.7, color="blue", edgecolor="black", alpha=0.5, label="Theoretical probability")
    legend(loc="lower left")
    xticks(range(min(x), max(x) + 1))
    grid()
    show()


def ex2():
    # Uber die Zufallsgroße X ist Anzahl von Fehlern in den online Artikeln einer bestimmten Zeitung ist bekannt:
    # in 25% der Artikeln sind keine Tippfehler, in 35% der Artikel ist ein Tippfehler, in 25% der Artikel sind zwei, in
    # 10% drei und auf dem Rest vier Tippfehler.
    # a) Man generiere zufallige Werte fur X.
    simulations = 1000
    errors = [0, 1, 2, 3, 4]
    probability = [0.25, 0.35, 0.25, 0.10, 0.05]
    rng = numpy.random.default_rng()
    data = rng.choice(errors, size=simulations, replace=True, p=probability)
    values, count = numpy.unique(data, return_counts=True)

    # b) Man schatze anhand der Simulationen die Wahrscheinlichkeit, dass hochstens 1 Tippfehler in einem zufallig
    # gewahlten Artikel auftaucht.
    print(f"Probability of max 1 error: {(count[0] + count[1]) / simulations}")

    # c) Wie viele Tippfehler sind durchschnittlich (im Mittel) in einem online Artikel dieser Zeitung zu erwarten, d.h.
    # man verlangt die Schatzung von dem Erwartungswert E(X). Man berechne den theoretischen Erwartungswert.
    print(f"Average error count: {numpy.mean(data)}")
    print(f"Theoretical average error count: {sum(x * p for x, p in zip(errors, probability))}")


def ex3():
    n = 1000
    max_value = 8
    probability = 0.5
    all_values = []

    for i in range(max_value + 1):
        all_values.append(i)

    x = binom.rvs(max_value, probability, size=n)
    w = binom.pmf(all_values, max_value, probability)

    bar(all_values, w, width=0.9, color="red", edgecolor="black", label="Theor. Haufigkeiten ")
    xticks(range(0, max_value + 1))

    xx, count = numpy.unique(x, return_counts=True)
    bar(xx, count / n, width=0.6, color="blue", edgecolor="black", label="Rel. Haufigkeiten ")

    legend(loc="upper right")

    grid()
    show()


def ex4():
    # In einem Computerpool sind 7 Rechner. Die Wahrscheinlichkeit, dass ein neuer Virus
    # einen Rechner angreift ist 0.4, unabhangig von anderen Rechnern.
    #
    # Man gebe die Antworten anhand Simulationen (binom.rvs) und vergleiche diese mit den theoretischen
    # Wahrscheinlichkeiten (hierfur benutze man binom.cdf, binom.pmf).

    simulations = 1000
    nr_computers = 7
    probability = 0.4
    values_sim = binom.rvs(nr_computers, probability, size=simulations)

    # Welche ist die Wahrscheinlichkeit, dass der Virus:
    # a) hochstens 3 Rechner
    count = 0
    for value in values_sim:
        if value <= 3:
            count += 1
    print(f"Max 3 computers (simulation): {count / simulations}")
    theoretical = binom.cdf(3, nr_computers, probability)
    print(f"Theoretical: {theoretical:.3f}")

    # b) mindestens 4 Rechner
    count = 0
    for value in values_sim:
        if value >= 4:
            count += 1
    print(f"Min 4 computers (simulation): {count / simulations}")
    theoretical = 1 - binom.cdf(3, nr_computers, probability)
    print(f"Theoretical: {theoretical:.3f}")

    # c) genau 4 Rechner angreift?
    count = 0
    for value in values_sim:
        if value == 4:
            count += 1
    print(f"Genau 4 computers (simulation): {count / simulations}")
    theoretical = binom.pmf(4, nr_computers, probability)
    print(f"Theoretical: {theoretical:.3f}")


def ex5():
    # Anzahl der Simulationen
    num_simulations = 500

    results = []
    for _ in range(num_simulations):
        generated_numbers = random.choice(arange(1, 6), size=1000, p=[1 / 5] * 5)
        # Suche nach der Position der ersten 5 in den generierten Zahlen
        first_occurrence_index = argmax(generated_numbers == 5)
        # Anzahl der generierten Zahlen vor der ersten 5
        x = first_occurrence_index + 1
        results.append(x)

    hist(results, bins=arange(1, max(results) + 2) - 0.5, density=True, edgecolor='black')
    title('Histogram of X: Number of Generated Numbers before First 5')
    xlabel('X')
    ylabel('Probability')
    show()

    # P(X ≤ 3)
    probability_x_leq_3 = mean(array(results) <= 3)
    # P(X > 3)
    probability_x_gt_3 = mean(array(results) > 3)
    # Erwartungswert E(X)
    expectation_x = mean(results)
    # Schätzung durchführen
    # Ergebnisse ausgeben
    print(f"Estimated Probability P(X <= 3): {probability_x_leq_3}")
    print(f"Estimated Probability P(X > 3): {probability_x_gt_3}")
    print(f"Estimated Expectation E(X): {expectation_x}")


def main():
    ex1()
    ex2()
    ex3()
    ex4()
    ex5()


if __name__ == "__main__":
    main()

import random

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, expon, uniform


def ex1():
    # Teepackungen, die von einer bestimmten Firma abgefullt werden, sollten mit jeweils 200 g Inhalt
    # abgefullt werden. Die abgefullte Menge Tee X in einer Packung ist normal verteilt X ∼ N(µ, σ^2); die dafur
    # zustandige Abfullmaschine hat eine Standardabweichung von σ = 3 g und ist auf einen Erwartungswert
    # µ = 199 g eingestellt
    # a) Anhand 1000 simulierten Daten, welche ist im Mittel die abgefullte Menge Tee in einer Packung?
    mu = 199
    sigma = 3
    n = 10000
    data = norm.rvs(mu, sigma, n)
    average = np.mean(data)
    print("Average:", average)

    # b)
    # Mit welcher Wahrscheinlichkeit werden in einer Packung weniger als 195 g Tee abgefullt?
    # Mit welcher Wahrscheinlichkeit werden in einer Packung zwischen 195 g und 198 g Tee abgefullt?
    # Mit welcher Wahrscheinlichkeit werden in einer Packung mehr als 195 g Tee abgefullt?
    print(f"Probability to have less than 195 g: {sum(data <= 195) / n}")
    print(f"Probability to have between 195 and 198 g: {np.mean((data >= 195) * (data <= 198)) / n}")
    print(f"Probability to have more than 195 g: {sum(data > 195) / n}")

    # Man vergleiche das Ergebnis mit den theoretischen Wahrscheinlichkeiten.
    print(f"The probability to have less than 195 g is: {norm.cdf(195, mu, sigma)}")
    print(f"The probability to have between 195 and 198 g is: {norm.cdf(198, mu, sigma) - norm.cdf(195, mu, sigma)}")
    print(f"The probability to have more than 195 g is: {1 - norm.cdf(195, mu, sigma)}")

    # c) Die generierten Daten der Stichprobe sollen in 16 Klassen (Intervallen) eingeteilt.
    # Man zahle mit Hfg, Klasse=numpy.histogram(Daten, bins=16) und gebe an (mit print) wie viele Daten in jeder
    # Klasse sind.
    hfg, klasse = np.histogram(data, bins=16)
    print("Histogram:")
    for i, (count, interval) in enumerate(zip(hfg, klasse)):
        print(f"({i + 1}) absolute Hfg. {count} der Klasse {interval}")

    # Man zeichne das entsprechende Histogramm der relativen Haufigkeiten mit
    # matplotlib.pyplot.hist(Daten,bins=16,density=True, edgecolor="black", label="rel. Hfg.")
    # Auf demselben Bild zeichne man auch die Dichtefunktion der N(µ, σ^2) Verteilung (µ = 199, σ = 3).
    # Hinweis: Man benutze scipy.stats.norm.pdf(x, µ, σ)) und plot.
    plt.hist(data, bins=16, density=True, edgecolor="black", label="rel. Hfg.")
    x = np.linspace(min(data), max(data), 100)
    pdf_values = norm.pdf(x, mu, sigma)
    plt.plot(x, pdf_values)
    plt.show()


def ex2():
    # Die Zeit T (in Sekunden), die ein Drucker benotigt, um ein Werbeplakat zu drucken, folgt einer
    # Exponentialverteilung Exp(α) mit dem Parameter α = 1/12

    # a) Man simuliere N = 1000 Daten fur eine Stichprobe.
    # Welche ist die durchschnittliche Druckzeit fur das Drucken eines Plakats?
    n = 1000
    alpha = 1 / 12
    data = expon.rvs(loc=0, scale=1 / alpha, size=n)
    mean = np.mean(data)
    print("Mean is: ", mean)

    # b) Man zeichne ein Histogramm mit 12 Klassen fur die simulierten Daten und auf demselben Bild zeichne
    # man die Dichtefunktion scipy.stats.expon.pdf(x,loc=0,scale=1/alpha).
    hist, bins, _ = plt.hist(data, bins=12, density=True, edgecolor='black', label='Histogram')
    x = np.linspace(min(bins), max(bins), 1000)
    pdf_values = expon.pdf(x, loc=0, scale=1 / alpha)
    plt.plot(x, pdf_values, label='Exponential PDF')
    plt.title('Histogram and Exponential PDF of Print Time')
    plt.xlabel('Print Time (seconds)')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.show()
    # Additional part for printing class information
    hfg, klassen = np.histogram(data, bins=12)
    for i in range(len(hfg)):
        print(f"Klasse {i + 1:2d}: {hfg[i]:3d} Daten, [{bins[i]:8.4f}, {bins[i + 1]:8.4f}]")

    # c) Man schatze danach die Wahrscheinlichkeiten P(T < 20), P(T > 10), P(10 < T < 30).
    probability_less_than_20 = np.mean(data < 20)
    probability_greater_than_10 = np.mean(data > 10)
    probability_between_10_and_30 = np.mean((data > 10) & (data < 30))

    # Man vergleiche das Ergebnis mit den theoretischen Wahrscheinlichkeiten, welche man mit
    # scipy.stats.expon.cdf(x,loc=0,scale=1/alpha) berechnet.
    theoretical_probability_less_than_20 = expon.cdf(20, loc=0, scale=1 / alpha)
    theoretical_probability_greater_than_10 = 1 - expon.cdf(10, loc=0, scale=1 / alpha)
    theoretical_probability_between_10_and_30 = expon.cdf(30, loc=0, scale=1 / alpha) - expon.cdf(10, loc=0,
                                                                                                  scale=1 / alpha)

    print(f"Estimated Probability T < 20: {probability_less_than_20}")
    print(f"Theoretical Probability T < 20: {theoretical_probability_less_than_20}\n")

    print(f"Estimated Probability T > 10: {probability_greater_than_10}")
    print(f"Theoretical Probability T > 10: {theoretical_probability_greater_than_10}\n")

    print(f"Estimated Probability 10 < T < 30: {probability_between_10_and_30}")
    print(f"Theoretical Probability 10 < T < 30: {theoretical_probability_between_10_and_30}")

    # d) Die generierten Daten der Stichprobe wurden in 12 Klassen (Intervallen) eingeteilt. Man zahle und
    # gebe an wie viele Daten in jeder Klasse sind, und man zeichne auf einem neuen Bild das entsprechende
    # Histogramm der absoluten Haufigkeiten.
    # matplotlib.pyplot.hist(Daten,bins=12,density=False,edgecolor="black",label="absolute Hfg.")
    absolute_hfg, bins = np.histogram(data, bins=12)

    # Print the counts in each class
    for i in range(len(absolute_hfg)):
        print(f"Klasse {i + 1:2d}: {absolute_hfg[i]:3d} Daten, [{bins[i]:8.4f}, {bins[i + 1]:8.4f}]")

    # Draw the histogram of absolute frequencies
    plt.hist(data, bins=12, density=False, edgecolor="black", label="absolute Hfg.")
    plt.xlabel('T')
    plt.ylabel('Absolute Frequency')
    plt.title('Histogram of Absolute Frequencies')
    plt.legend()
    plt.show()

    # e) Auf einem anderen Bild zeichne man auf dem Intervall [0, 10] die Dichtefunktion der Exp(1) Verteilung.
    # Generate x values for the plot
    x_values = np.linspace(0, 10, 100)

    # Calculate the corresponding y values using the density function of Exp(1)
    y_values = expon.pdf(x_values, loc=0, scale=1)

    # Plot the density function
    plt.plot(x_values, y_values, 'r-', label='Density Function (Exp(1))')

    # Set plot labels and title
    plt.xlabel('T')
    plt.ylabel('Density')
    plt.title('Density Function of Exp(1) Distribution')
    plt.legend()
    plt.show()


def ex3():
    num_simulations = 1000
    total_profit = 0
    total_wins = 0
    for _ in range(num_simulations):
        birthdays = [np.random.randint(1, 13) for _ in range(6)]
        if len(birthdays) != len(set(birthdays)):
            total_wins += 1
            total_profit += 6
        else:
            total_profit -= 6
    avg_profit = total_profit / num_simulations
    win_probability = total_wins / num_simulations
    print(f"Average Profit: {avg_profit}")
    print(f"Win probability: {win_probability}")


def ex4():
    # In einer Urne sind 4 weiße und 6 schwarze Kugeln. Ein Spieler zieht nacheinander eine Kugel
    # ohne Zurucklegen. Das Spiel ist aus, wenn er eine weisse Kugel zieht oder wenn er dreimal gezogen hat.
    # Die Zufallsvariable X zeigt die Anzahl der gezogenen schwarzen Kugeln.
    # a) Welches ist die (theoretische) Wahrscheinlichkeitsverteilung von X und simuliere zufallige Werte fur X.
    # b) Der Spieler erhalt 30 Punkte, wenn er drei schwarze Kugeln gezogen hat. Er erhalt 25 Punkte, wenn er
    # zwei schwarze Kugeln zieht. In allen anderen Fallen verliert er 5 Punkte. Anhand Simulationen schatze
    # man die mittlere Punktezahl des Spielers. Man vergleiche das Ergebnis mit dem theoretischen Ergebnis.
    print("Theoretische:")
    print(f"P(X = 0) = P(erste Kugel ist weiß) = {4 / 10}")
    print(f"P(X = 1) = P(erste Kugel schwarz, zweite Kugel weiß) = {6 / 10 * 4 / 9}")
    print(f"P(X = 2) = P(erste und zweite Kugel schwarz, dritte Kugel weiß) = {6 / 10 * 5 / 9 * 4 / 8}")
    print(f"P(X = 3) = P(erste und zweite und dritte Kugel schwarz) = {6 / 10 * 5 / 9 * 4 / 8}")

    num_simulations = 1000
    count_black_0 = 0
    count_black_1 = 0
    count_black_2 = 0
    count_black_3 = 0
    score = 0
    for _ in range(num_simulations):
        balls = random.sample(['w', 's'], counts=[4, 6], k=3)
        if balls[0] == 'w':
            count_black_0 += 1
            score -= 5
        elif balls[1] == 'w':
            count_black_1 += 1
            score -= 5
        elif balls[2] == 'w':
            count_black_2 += 1
            score += 25
        else:
            count_black_3 += 1
            score += 30
    print("Relative:")
    print(f"P(X = 0) = P(erste Kugel ist weiß) = {count_black_0 / num_simulations:.2f}")
    print(f"P(X = 1) = P(erste Kugel schwarz, zweite Kugel weiß) = {count_black_1 / num_simulations:.2f}")
    print(f"P(X = 2) = P(erste und zweite Kugel schwarz, dritte Kugel weiß) = {count_black_2 / num_simulations:.2f}")
    print(f"P(X = 3) = P(erste und zweite und dritte Kugel schwarz) = {count_black_3 / num_simulations:.2f}")

    print(f"P(Y = 30) = {count_black_3 / num_simulations:.2f}")
    print(f"P(Y = 25) = {count_black_2 / num_simulations:.2f}")
    print(f"P(Y = -5) = {(count_black_0 + count_black_1) / num_simulations:.2f}")
    print(f"E(Y) = Average score: {score / num_simulations}")


def ex5():
    # Man simuliere mit Hilfe von scipy.stats.uniform.rvs 1000 zuf¨allige Punkte aus dem Quader
    # [−1, 1] × [−1, 1] × [−1, 1] ⊂ R^3
    # Sei D die ZG welche Distanz dieser Punkte zum Ursprung (0,0,0) darstellt.
    # Man schatze den Erwartungswert (numpy.mean) und die Varianz von D (numpy.var).
    num_points = 1000
    # Generate random points in the cube [-1, 1] × [-1, 1] × [-1, 1]
    points = uniform.rvs(loc=-1, scale=2, size=(num_points, 3))
    # Calculate the distance to the origin for each point
    distances = np.linalg.norm(points, axis=1)
    # Calculate the mean and variance of distances
    mean_distance = np.mean(distances)
    variance_distance = np.var(distances)
    print(f"Estimated Mean Distance: {mean_distance:.4f}")
    print(f"Estimated Variance of Distance: {variance_distance:.4f}")


def main():
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    ex5()


if __name__ == "__main__":
    main()

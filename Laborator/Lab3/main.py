import random
from enum import unique
from math import comb

import numpy
from matplotlib.pyplot import bar, show, grid, legend, xticks
from numpy import count_nonzero, unique


def ex1_1():
    # In einer Urne sind 6 rote Kugeln, 4 blaue Kugeln und 6 gr¨une Kugeln. Man zieht 3 Kugeln
    # hintereinander ohne Zurucklegen. Man betrachtet die Ereignisse:
    # A:“mindestens eine rote Kugel wurde entnommen”
    # B:“alle entnommenen Kugeln haben dieselbe Farbe”.
    # 1) Anhand Simulationen schatze man die Wahrscheinlichkeiten P(A), P(B), P(A ∩ B), P(B|A).
    num_simulations = 1000
    red_count = 6
    blue_count = 4
    green_count = 6
    successful_a = 0
    successful_b = 0
    successful_ab = 0
    for _ in range(num_simulations):
        balls = random.sample(['r', 'b', 'g'], counts=[red_count, blue_count, green_count], k=3)
        extracted_balls = random.sample(balls, k=3)
        if 'r' in extracted_balls:
            successful_a += 1

        if extracted_balls[0] == extracted_balls[1] == extracted_balls[2]:
            if 'r' in extracted_balls:
                successful_ab += 1
            successful_b += 1

    print(f"A: P(A) = {successful_a / num_simulations}")
    print(f"B: P(B) = {successful_b / num_simulations}")
    print(f"C: P(A and B) = {successful_ab / num_simulations}")
    print(f"D: P(B|A)= {(successful_ab / num_simulations) / (successful_a / num_simulations)}")


def ex1_2():
    # 2) Man gebe auch die theoretischen Wahrscheinlichkeiten an f¨ur P(A), P(B), P(A ∩ B), P(B|A).
    #           not red extracted
    th_A = 1 - (10 / 16 * 9 / 15 * 8 / 14)
    #      all red                    all blue                  all green
    th_B = (6 / 16 * 5 / 15 * 4 / 14) + (4 / 16 * 3 / 15 * 2 / 14) + (6 / 16 * 5 / 15 * 4 / 14)
    th_AB = 6 / 16 * 5 / 15 * 4 / 14
    th_BA = th_AB / th_A

    print(f"Theoretical probability P(A) = {th_A}")
    print(f"Theoretical probability P(B) = {th_B}")
    print(f"Theoretical probability P(A and B) = {th_AB}")
    print(f"Theoretical probability P(B|A) = {th_BA}")


def ex2():
    # Beispiel Histogramm - Man zeichne ein Histogramm der relativen Haufigkeiten der Zahlen
    # die beim 200-maligen Wurfeln erhalten wurden. Was stellt das blau gezeichnete Histogramm dar?
    # Wie verandert sich das Bild wenn N = 2000?
    n = 20000
    data = [random.randrange(1, 7) for _ in range(n)]
    results, count = numpy.unique(data, return_counts=True)
    d = dict([(results[i], count[i] / n) for i in range(0, 6)])
    print(d)
    bar(results, count / n, width=0.9, color="red", edgecolor="black", label="Relative probability")
    d = dict([(k, 1 / 6) for k in range(1, 7)])
    bar(d.keys(), d.values(), width=0.7, color="blue", edgecolor="black", label="Theoretical probability")
    legend(loc="lower left")
    xticks(range(0, 7))
    grid()
    show()


def ex3():
    # Drei Wurfel werden geworfen. Das Spiel gewinnt derjenige, der die Summe der drei aufgetauchten Zahlen vorhersagt.
    # (1) Man simuliere dieses Spiel N-mal (=500, 1000...), man erstelle das Histogramm der relativen
    # Haufigkeiten. Auf demselben Bild zeichne man auch die Balken f¨ur die theoretischen Wahrscheinlichkeiten.
    # Man vergleiche die theoretischen Ergebnisse mit den erhaltenen Werten aus den Simulationen.
    simulations_count = 500
    dice1 = [random.randrange(1, 7) for _ in range(simulations_count)]
    dice2 = [random.randrange(1, 7) for _ in range(simulations_count)]
    dice3 = [random.randrange(1, 7) for _ in range(simulations_count)]
    dice_sums = []
    # simulate n games
    for i in range(simulations_count):
        dice_sums.append(dice1[i] + dice2[i] + dice3[i])

    # print the relative probability
    results, count = numpy.unique(dice_sums, return_counts=True)
    relative_probability = dict([(results[i], count[i] / simulations_count) for i in range(len(results))])
    bar(results, count / simulations_count, width=0.9, color="red", edgecolor="black", label="Relative probability")

    # calculate the theoretical probability
    dice_sums_theoretical = []
    for i in [1, 2, 3, 4, 5, 6]:
        for j in [1, 2, 3, 4, 5, 6]:
            for k in [1, 2, 3, 4, 5, 6]:
                dice_sums_theoretical.append(i + j + k)

    results, count = numpy.unique(dice_sums_theoretical, return_counts=True)
    bar(results, count / (6 * 6 * 6), width=0.7, color="blue", edgecolor="black", label="Theoretical probability")

    # (2) Auf welche Zahl (oder Zahlen) muss man wetten, um die großten Gewinnchancen zu haben?
    best_choices_relative_array = best_choices(count)
    print(f"Best relative choice: {best_choices_relative_array}")

    best_choices_theoretical_array = best_choices(count)
    print(f"Best theoretical choice: {best_choices_theoretical_array}")

    legend(loc="lower left")
    xticks(range(0, 19))
    grid()
    show()

    # (3) Welches ist die theoretische Wahrscheinlichkeit, dass diese Zahl (oder Zahlen) auftaucht? Man
    # vergleiche das theoretische Resultat mit den erhaltenen Ergebnissen der Simulationen.
    count_relative = 0
    dice_sums_unique = unique(dice_sums)
    for number in best_choices_relative_array:
        count_relative += count_nonzero(dice_sums_unique == number)

    print(f"Probability of best choice in relative (simulation): {count_relative / len(dice_sums_unique)}")

    count_theoretical = 0
    dice_sums_theoretical_unique = unique(dice_sums_theoretical)
    for number in best_choices_theoretical_array:
        count_theoretical += count_nonzero(dice_sums_theoretical_unique == number)

    print(f"Probability of best choice in theory: {count_theoretical / len(dice_sums_theoretical_unique)}")


def best_choices(count):
    max_count = max(count)
    max_positions = []
    for i in range(len(count)):
        if count[i] == max_count:
            max_positions.append(i + 3)
    return max_positions


def ex4():
    # Welche Wahrscheinlichkeiten p1, p2, p3 schatzt folgendes Programm?
    # Welche sind die theoretischen Werte fur p1, p2, p3?
    c1, c2, a1, a2 = 0, 0, 0, 0
    n = 10000
    a = list(range(1, 21))
    for _ in range(n):
        i = numpy.random.randint(len(a))
        v = a[i]
        c1 = c1 + (v % 2)
        c2 = c2 + ((v % 2) == 0)
        a1 = a1 + (v % 2) * ((v % 3) == 0)
        a2 = a2 + ((v % 2) == 0) * (6 <= v <= 10)
    p1 = a1 / c1
    p2 = a2 / c2
    p3 = c1 / n
    print("Aus den Simulationen :")
    print(f"p1=", p1)
    print(f"p2=", p2)
    print(f"p3=", p3)


def ex5():
    # Welche ist die Wahrscheinlichkeit, dass in einer Gruppe von 5 Personen genau zwei Personen
    # Geburtstag im selben Monat haben und die anderen drei Personen verschiedene Geburtstage haben?
    # a) Man lose die Aufgabe anhand Simulationen.
    num_simulations = 100000
    count_successful = 0  # Zählt die erfolgreichen Simulationen
    for _ in range(num_simulations):
        birthdays = [random.randint(1, 12) for _ in range(5)]  # Zufällige Auswahl von Geburtsmonaten
        # Überprüfen, ob genau zwei Personen im selben Monat Geburtstag haben und die anderen drei verschieden sind
        if len(birthdays) == len(set(birthdays)) + 1:
            count_successful += 1
    probability = count_successful / num_simulations
    print(f"Simulierte Wahrscheinlichkeit: {probability}")

    # b) Man gebe die theoretische Wahrscheinlichkeit an. Annahme:
    # die Wahrscheinlichkeit, dass eine zufallig gewahlte Person Geburtstag in einem bestimmten Monat hat ist 1/12
    total_outcomes = 12 ** 5
    ways_two_shared = comb(5, 2)
    ways_remaining = 11 * 10 * 9
    probability = ways_two_shared * ways_remaining / total_outcomes
    print(f"Thoretical probability: {probability}")


def ex6():
    # Man schatze anhand Simulationen die Wahrscheinlichkeit, dass beim zweimaligen Werfen eines
    # Wurfels die Summe der Zahlen mindestens 7 ist (Summe ≥ 7),
    # a) unter der Bedingung, dass beim ersten Wurf eine 4 erhalten wurde;\
    num_simulations = 100000
    count_successful = 0
    for _ in range(num_simulations):
        first_throw = 4
        second_throw = random.randint(1, 6)
        if first_throw + second_throw >= 7:
            count_successful += 1
    probability = count_successful / num_simulations
    print(f"Simulierte Wahrscheinlichkeit unter Bedingung a): {probability}")

    # b) unter der Bedingung, dass beim zweiten Wurf eine gerade Zahl erhalten wurde.
    num_simulations = 100000
    count_successful = 0
    for _ in range(num_simulations):
        first_throw = random.randint(1, 6)
        second_throw = random.choice([2, 4, 6])
        if first_throw + second_throw >= 7:
            count_successful += 1
    probability = count_successful / num_simulations
    print(f"Simulierte Wahrscheinlichkeit unter Bedingung b): {probability}")

    # c) Welche sind die theoretischen Wahrscheinlichkeiten bei a), bzw. b) ?
    # a) begins with 4 => 3, 4, 5 or 6 are needed => probability = 4/6
    # b) case 1: 2 => 5, 6              => 2/6
    #    case 2: 4 => 3, 4, 5, 6        => 4/6      => probability = 2/6 + 4/6 + 6/6
    #    case 3: 6 => 1, 2, 3, 4, 5, 6  => 6/6


def main():
    # ex1_1()
    # ex1_2()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    ex6()


if __name__ == "__main__":
    main()

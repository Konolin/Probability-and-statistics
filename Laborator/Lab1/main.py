import itertools
import math
import random


def main():
    # 2.
    # a) Man erstelle eine Liste mit den Permutationen von ABC.
    s = "ABC"
    permutation_list = list(itertools.permutations(s))
    print(permutation_list)

    # b) Welches ist die gesamte Anzahl der Permutationen von ABC?
    print(math.perm(len(s)))

    # c) Man generiere eine zufällige Permutation von MATHE.
    s = "MATHE"
    print(random.sample("MATHE", 5))

    # d) Man generiere eine zufällige Variation mit 3 Buchstaben aus dem String MATHE.
    print(random.sample("MATHE", 3))

    # e) Man generiere alle Variationen (d.h. Anordnungen ohne Wiederholung, mit Berücksichtigung der Reihenfolge)
    # mit 3 Buchstaben aus dem String MATHE (d.h. alle Variationen je 3 Buchstaben aus dem String MATHE).
    variations = list(itertools.permutations("MATHE", 3))
    print(variations)

    # f) Welches ist die gesamte Anzahl der Variationen je 3 Buchstaben von MATHE?
    print(math.perm(len("ABC"), 3))

    # g) Man generiere alle Kombinationen (d.h. alle Anordnungen ohne Wiederholung, ohne Berücksichtigung der
    # Reihenfolge) mit 3 Buchstaben aus dem String MATHE (d.h. alle Kombinationen je 3 Buchstaben aus dem String
    # MATHE).
    combination = list(itertools.combinations("MATHE", 3))
    print(combination)

    # h) Welches ist die gesamte Anzahl der Kombinationen je 3 Buchstaben von MATHE?
    # Hinweis: math.comb
    print(math.comb(len("MATHE"), 3))

    # Wie viele Möglichkeiten gibt es 6 rote Kugeln in 4 Kartons aufzuteilen? Manche Kartons konnten leer
    # bleiben. Man zahle alle möglichen Anordnungen auf. Hinweis: Wir bezeichnen die vier Kartons mit 1,2,3,4.
    # Eine mögliche Anordnung ist: [1,1,2,3,3,3], d.h. 2 Kugeln im Karton ”1”, eine Kugel im Karton ”2”, 3 Kugeln
    # im Karton ”3” und keine Kugel im Karton ”4”.
    kartons = [1, 2, 3, 4]
    kombinationen = itertools.combinations_with_replacement(kartons, 6)
    n = 0
    for i in kombinationen:
        n += 1
        print(i)
    print(f"Es gibt {n} Möglichkeiten")


if __name__ == '__main__':
    main()

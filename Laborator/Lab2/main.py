from math import dist
from numpy import random, unique, square, power, linalg, array
from matplotlib.pyplot import axis, plot, figure, show, legend
from matplotlib.patches import Circle


def same_birthday():
    # two people in a group of 23 people have the same birthday
    array = random.randint(1, 366, 23)
    return len(array) != len(unique(array))


def ex1():
    positive_outcome = 0
    tries = 10000
    for i in range(tries):
        if same_birthday():
            positive_outcome += 1
    return positive_outcome / tries


def ex1_theoretic():
    p = 1
    for i in range(343, 366):
        p *= i / 365
    return 1 - p


def example():
    fig = figure()
    axis("square")
    axis((0, 1, 0, 1))
    x = random.random(25)
    y = random.random(25)
    plot(x, y, "bo")
    fig.suptitle("Beispiel 1 ", fontweight="bold")
    show()
    fig = figure()
    axis("square")
    axis((0, 1, 0, 1))
    plot(x, square(x), "g*")  # zufallige Punkte auf dem Bild der Funktion F(x)=xˆ2
    plot(x, power(x, 4), "mo")  # zufallige Punkte auf dem Bild der Funktion F(x)=xˆ4
    plot(x[-1], square(x[-1]), "g*", label="xˆ2")
    plot(x[-1], power(x[-1], 4), "mo", label="xˆ4")
    legend(loc='upper left')
    fig.suptitle("Beispiel 2 ", fontweight="bold")
    show()


def ex2(n):
    # create table
    fig = figure()
    axis("square")
    axis((0, 1, 0, 1))

    # generate the coordinates for n points
    x = random.random(n)
    y = random.random(n)

    # draw the circle with the center at 0.5, 0.5 and radius of 0.5
    circle = Circle((0.5, 0.5), 0.5, fill=False, color='r')
    ax = fig.gca()
    ax.add_patch(circle)

    # draw them based on their position relative to the circle
    # count in k how many are inside the circle
    k = 0
    for i in range(len(x)):
        if dist([0.5, 0.5], [x[i], y[i]]) > 0.5:
            plot(x[i], y[i], "bo")
        else:
            plot(x[i], y[i], "ro")
            k += 1

    # show the table
    fig.suptitle("Ex 2 ", fontweight="bold")
    show()

    # calculate the probability of the points to be inside the circle
    probability = k / n
    print(f"The probability of a point to bi inside the circle : {probability}")

    # approx pi
    print(f"pi is approx : {4 * probability}")


def is_obtuse_triangle(x, y):
    # Überprüfen, ob das Dreieck mit den Koordinaten x und y einen stumpfen Winkel hat
    sides = [
        linalg.norm(x - y),
        linalg.norm(x),
        linalg.norm(y)
    ]
    sides.sort()
    return sides[0] ** 2 + sides[1] ** 2 < sides[2] ** 2


def ex3(n):
    a, b, c, d = [0, 0], [1, 0], [1, 1], [0, 1]
    axis('square')
    axis((0, 1, 0, 1))
    count1 = 0
    count2 = 0
    for _ in range(n):
        x = [random.random(), random.rand()]
        da, db, dc, dd = dist(x, a), dist(x, b), dist(x, c), dist(x, d)
        st = (da ** 2 + db ** 2 < 1) + ()


def main():
    print(f"ex1 : {ex1()}")
    print(f"ex1_theoretic : {ex1_theoretic():.6f}")
    # example()
    # ex2(1000)
    ex3(1000)


main()

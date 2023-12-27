from math import dist

from matplotlib.patches import Circle
from matplotlib.pyplot import axis, plot, figure, show, legend, scatter, xlabel, ylabel, title, colorbar
from numpy import random, unique, square, power, linalg, array


def same_birthday():
    # two people in a group of 23 people have the same birthday
    birthday_array = random.randint(1, 366, 23)
    return len(birthday_array) != len(unique(birthday_array))


def ex1():
    # a) Man schatze durch wiederholte Simulationen die Wahrscheinlichkeit von dem Ereignis
    # A: in einer Gruppe von k = 23 Personen mindestens zwei Personen haben den gleichen Geburtstag.
    # Annahme: Das Jahr hat n = 365 Tage.
    positive_outcome = 0
    tries = 10000
    for i in range(tries):
        if same_birthday():
            positive_outcome += 1
    return positive_outcome / tries


def ex1_theoretic():
    # Man berechne die theoretische Wahrscheinlichkeit P(A) ?
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
    # Man mochte die Wahrscheinlichkeit schatzen, dass ein zufallig
    # gewahlter Punkt im Quadrat [0, 1] × [0, 1] sich auch in dem
    # eingeschriebenen Kreis befindet (siehe Bild).

    # create table
    fig = figure()
    axis("square")
    axis((0, 1, 0, 1))

    # (2a) Man simuliere N zufallige Punkte im Quadrat und man zahle wie viele im Kreisinneren sind; sei k diese
    # Zahl. Man zeichne auf demselben Bild die zufalligen Punkte mit verschiedenen Farben: diejenigen die im bzw.
    # die außhalb des Kreisinneren sind. Hinweis: fur die euklidische Distanz zwischen zwei Punkten kann man
    # math.dist benutzen.

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

    # (2b) Welches ist die Wahrscheinlichkeit, dass der Punkt im Kreisinneren ist?
    # [Der theoretische Wert ist π/4, bzw. die Approximation ist k/N]
    probability = k / n
    print(f"The probability of a point to bi inside the circle : {probability}")

    # (2c) Anhand von (2a) und (2b) gebe man verschiedene Approximationen von π an.
    # [Hinweis: π ≈ 4 * k/N]
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


def ex3(num_simulations):
    # 3) Im Inneren eines Quadrates mit Seitenlange 1 wahlt man zufallig einen Punkt A. Man verbindet A mit den
    # Spitzen des Quadrates und man erhalt vier Dreiecke mit gemeinsamer Spitze in A. Anhand von Simulationen
    # beantworte man folgende Fragen:
    # (1) Welches ist die Wahrscheinlichkeit, dass genau ein Winkel in A stumpf ist?
    # (2) Welches ist die Wahrscheinlichkeit, dass genau zwei Winkel in A stumpf sind?
    # Man zeichne auf demselben Bild die zufalligen Punkte (entsprechend den Fallen (1), (2)) mit verschiedenen Farben.

    # Corners of the square
    a, b, c, d = [0, 0], [1, 0], [1, 1], [0, 1]

    # Initialize counts for each case
    count1 = 0  # Count of triangles with exactly one obtuse angle
    count2 = 0  # Count of triangles with exactly two obtuse angles

    # Initialize plot
    figure()
    axis('square')
    axis((0, 1, 0, 1))

    for _ in range(num_simulations):
        # Randomly choose a point A inside the unit square
        x = [random.random(), random.random()]

        # Calculate distances from A to the corners
        da, db, dc, dd = dist(x, a), dist(x, b), dist(x, c), dist(x, d)

        # Check if each angle in the formed triangles is obtuse
        angles = [
            da ** 2 + db ** 2 < 1,
            db ** 2 + dc ** 2 < 1,
            dc ** 2 + dd ** 2 < 1,
            dd ** 2 + da ** 2 < 1
        ]

        # Count the number of obtuse angles in each case
        obtuse_count = angles.count(True)

        # Update counts based on the number of obtuse angles
        if obtuse_count == 1:
            count1 += 1
            scatter(x[0], x[1], color='blue')  # Blue for exactly one obtuse angle
        elif obtuse_count == 2:
            count2 += 1
            scatter(x[0], x[1], color='red')  # Red for exactly two obtuse angles

        # Calculate probabilities
    prob_stumpf_one = count1 / num_simulations
    prob_stumpf_two = count2 / num_simulations

    # Display probabilities
    print("Probability of exactly one obtuse angle:", prob_stumpf_one)
    print("Probability of exactly two obtuse angles:", prob_stumpf_two)

    # Show the plot
    title('Monte Carlo Simulation for Obtuse Angles')
    xlabel('X-axis')
    ylabel('Y-axis')
    show()


def ex4(num_simulations):
    # Man schreibe ein Programm (in Python), in welchem ein Bild mit N = 500 roten zufalligen Punkten generiert
    # wird −→ wie im unteren Bild. Man schatze die Wahrscheinlichkeit, dass ein zufallig gewahlter Punkt aus dem
    # Quadrat sich im Inneren des unteren oder oberen Dreieckes befindet (wie im Bild).
    points = random.rand(num_simulations, 2)

    # Define the vertices of the upper and lower triangles
    upper_triangle = array([[0.2, 0.8], [0.8, 0.8], [0.5, 0.5]])
    lower_triangle = array([[0.2, 0.2], [0.8, 0.2], [0.5, 0.5]])

    # Check if each point is inside the upper or lower triangle
    inside_upper_triangle = array([is_inside_triangle(p, *upper_triangle) for p in points])
    inside_lower_triangle = array([is_inside_triangle(p, *lower_triangle) for p in points])

    # Combine the conditions to get points inside either triangle
    inside_either_triangle = inside_upper_triangle | inside_lower_triangle

    # Calculate the probability of a randomly chosen point being inside either triangle
    probability_inside_either_triangle = sum(inside_either_triangle) / N

    # Plot the points with different colors for inside and outside the triangles
    plot_points(points, inside_either_triangle)

    # Display the calculated probability
    print("Estimated probability of a point being inside either triangle:", probability_inside_either_triangle)


def plot_points(points, inside_triangle):
    figure()
    scatter(points[:, 0], points[:, 1], c=inside_triangle, cmap='viridis', marker='.')
    title('Points Inside Either Triangle')
    xlabel('X-axis')
    ylabel('Y-axis')
    colorbar(label='Inside Triangle')
    show()


def is_inside_triangle(p, a, b, c):
    # Check if point p is inside the triangle defined by vertices a, b, c
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    d1 = sign(p, a, b)
    d2 = sign(p, b, c)
    d3 = sign(p, c, a)

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not (has_neg and has_pos)


def main():
    # print(f"ex1 : {ex1()}")
    # print(f"ex1_theoretic : {ex1_theoretic():.6f}")
    # example()
    # ex2(1000)
    # ex3(1000)
    ex4(500)


if __name__ == '__main__':
    main()

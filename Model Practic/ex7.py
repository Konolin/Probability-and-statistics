# Man wählt zufällig Punkte im Inneren des Quadrats [0,2]x[0,2] (siehe das untere Bild). Man schätze durch
# Simulationen die Wahrscheinlichkeit, dass diese Punkte innerhalb des weißen Dreieckes sind. Man zeichne die
# Punkte im Inneren des weißen Dreiecks mit einer anderen Farben als die Punkte ausserhalb dieses Dreiecks. Welche
# ist die exakte (theoretische) Wahrscheinlichkeit? (Hinweis: man benutze die geometrische Wahrscheinlichkeit und
# man berechne die zugehörigen Flächeninhalte!)

from matplotlib.pyplot import axis, plot, figure, show
from numpy import random

num_simulations = 100

fig = figure()
axis((0, 2, 0, 2))
x = random.random(num_simulations) * 2
y = random.random(num_simulations) * 2

# Plot points
num_inside = 0
for i in range(len(x)):
    if x[i] <= y[i]:
        plot(x[i], y[i], "bo")
        num_inside += 1
    else:
        plot(x[i], y[i], "ro")

show()

print(f"Probability simulations {num_inside / num_simulations:.2f}")

area_triangle = 2 * 2 / 2
area_square = 2 * 2
print(f"Theoretical probability: {area_triangle / area_square}")



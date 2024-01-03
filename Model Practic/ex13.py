# Man wählt zufällige Punkte innerhalb des blauen Quadrates.
# Man schätze durch Simulationen die Wahrscheinlichkeit, dass dieser Punkt
# ausserhalb des Kreises mit Zentrum in (0,0) und
# Radius 1 ist (siehe Abbildung).
import math
import random

num_simulations = 100
inside_circle = 0
for _ in range(num_simulations):
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    dist = math.dist((0, 0), (x, y))
    if dist <= 1:
        inside_circle += 1
print("Probability simulations:", inside_circle / num_simulations)

area_circle = math.pi * 1 ** 2 / 4
area_square = 2 * 2
print("Theoretical probability:", area_circle / area_square)
